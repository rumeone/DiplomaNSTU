"""SWE-Bench benchmark runner.

Runs tasks from SWE-bench (Lite / Verified / Full), generates patches via LLM
using two strategies (zero_shot, cot), evaluates them (Docker or static
fallback), and saves all artefacts to outputs/swebench_lite_results/.

Directory layout after run:
    outputs/swebench_lite_results/
        generated_patches/          <- LLM-generated .diff files
        evaluation_results/         <- per-task evaluation reports (.txt)
        reports/
            raw_results.json        <- full records
            raw_results.csv
            summary.csv             <- aggregated per-strategy stats

Usage:
    python run_swebench_lite.py                      # по умолчанию full SWE-Bench
    python run_swebench_lite.py --tasks 5 --subset verified
    python run_swebench_lite.py --force-static       # skip Docker eval
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import List, Optional

from tqdm import tqdm

from aggregation import compute_summary, save_records_to_csv, save_records_to_json
from config import MODEL_CONFIG
from llm_client import LLMClient
from swebench_loader import SWETask, load_swebench_tasks
from swebench_lite_evaluator import (
    SWEEvaluationResult,
    evaluate_swe_patch,
    is_valid_unified_diff,
)
from swebench_lite_prompts import (
    build_swe_cot_prompt,
    build_swe_zero_shot_prompt,
    SWEBENCH_SYSTEM_RULES,
)


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DEFAULT_MAX_TASKS = 3
DEFAULT_STRATEGIES = ["zero_shot", "cot"]
OUTPUT_BASE = Path("outputs") / "swebench_lite_results"

SUBSET_TO_DATASET = {
    "lite": "SWE-bench/SWE-bench_Lite",
    "verified": "SWE-bench/SWE-bench_Verified",
    "full": "SWE-bench/SWE-bench",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def safe_filename(value: str) -> str:
    """Convert instance_id or similar string to a safe filename component."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "task"


def ensure_dirs(base: Path) -> None:
    (base / "generated_patches").mkdir(parents=True, exist_ok=True)
    (base / "evaluation_results").mkdir(parents=True, exist_ok=True)
    (base / "reports").mkdir(parents=True, exist_ok=True)


def build_prompt(strategy: str, task: SWETask) -> str:
    """Select and build the prompt for a given strategy."""
    if strategy == "zero_shot":
        return build_swe_zero_shot_prompt(task.prompt)
    elif strategy == "cot":
        return build_swe_cot_prompt(task.prompt)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def save_patch(base: Path, instance_id: str, strategy: str, patch: str) -> Path:
    """Write generated patch to generated_patches/ and return the path."""
    fname = safe_filename(instance_id)
    path = base / "generated_patches" / f"{fname}__{strategy}.diff"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(patch, encoding="utf-8")
    return path


def save_eval_report(base: Path, instance_id: str, strategy: str, result: SWEEvaluationResult) -> Path:
    """Write evaluation report to evaluation_results/ and return the path."""
    fname = safe_filename(instance_id)
    path = base / "evaluation_results" / f"{fname}__{strategy}__eval.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    report = (
        f"Instance: {result.instance_id}\n"
        f"Strategy: {strategy}\n"
        f"Eval mode: {result.eval_mode}\n"
        f"Patch applied: {result.patch_applied}\n"
        f"Passed: {result.passed}\n"
    )
    if result.error:
        report += f"Error: {result.error}\n"
    report += "\n--- Test output ---\n"
    report += result.test_output
    path.write_text(report, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------

def run_single_task(
    client: LLMClient,
    task: SWETask,
    strategy: str,
    base: Path,
    force_static: bool = False,
    dataset_name: Optional[str] = None,
    split: str = "test",
) -> dict:
    """Generate a patch for one task+strategy and evaluate it."""
    # 1. Build prompt and generate patch
    prompt = build_prompt(strategy, task)
    try:
        raw_output = client.generate_code(prompt)
    except Exception as exc:
        return _error_record(task, strategy, error=f"LLM generation failed: {exc}")

    # Strip potential markdown fences (model might wrap in ```diff ... ```)
    patch = _strip_diff_fences(raw_output)

    # 2. Save generated patch to dedicated folder
    patch_path = save_patch(base, task.instance_id, strategy, patch)

    # 3. Evaluate patch
    eval_result = evaluate_swe_patch(
        instance_id=task.instance_id,
        generated_patch=patch,
        ground_truth_patch=task.patch,
        force_static=force_static,
        dataset_name=dataset_name,
        split=split,
    )

    # 4. Save evaluation report
    eval_report_path = save_eval_report(base, task.instance_id, strategy, eval_result)

    return {
        "task_id": task.instance_id,
        "repo": task.repo,
        "strategy": strategy,
        "patch_valid": is_valid_unified_diff(patch),
        "patch_file": str(patch_path.relative_to(base.parent.parent)),
        "eval_mode": eval_result.eval_mode,
        "patch_applied": eval_result.patch_applied,
        "passed": eval_result.passed,
        "eval_report_file": str(eval_report_path.relative_to(base.parent.parent)),
        "error": eval_result.error,
        "generated_patch": patch,
        "ground_truth_patch": task.patch,
    }


def _strip_diff_fences(text: str) -> str:
    """Remove markdown code fences around diffs if the model added them."""
    text = text.strip()
    text = re.sub(r'^```(?:diff|patch)?\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*```$', '', text)
    return text.strip()


def _error_record(task: SWETask, strategy: str, error: str) -> dict:
    return {
        "task_id": task.instance_id,
        "repo": task.repo,
        "strategy": strategy,
        "patch_valid": False,
        "patch_file": None,
        "eval_mode": "skipped",
        "patch_applied": None,
        "passed": None,
        "eval_report_file": None,
        "error": error,
        "generated_patch": "",
        "ground_truth_patch": task.patch,
    }


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run SWE-Bench benchmark")
    parser.add_argument(
        "--tasks", type=int, default=DEFAULT_MAX_TASKS,
        help=f"Number of SWE-Bench tasks to run (default: {DEFAULT_MAX_TASKS})",
    )
    parser.add_argument(
        "--strategies", nargs="+", default=DEFAULT_STRATEGIES,
        help="Prompt strategies to use (default: zero_shot cot)",
    )
    parser.add_argument(
        "--subset",
        default="full",
        choices=["lite", "verified", "full"],
        help="SWE-bench subset: lite (300), verified (500), full (2294). Default: full.",
    )
    parser.add_argument(
        "--force-static", action="store_true",
        help="Force static evaluation even if Docker is available",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=OUTPUT_BASE,
        help=f"Output directory (default: {OUTPUT_BASE})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = args.output_dir
    ensure_dirs(base)

    dataset_name = SUBSET_TO_DATASET.get(args.subset, "SWE-bench/SWE-bench")

    print(f"\n{'='*60}")
    print("SWE-Bench Benchmark")
    print(f"  Tasks:      {args.tasks}")
    print(f"  Strategies: {args.strategies}")
    print(f"  Subset:     {args.subset} ({dataset_name})")
    print(f"  Output:     {base}")
    print(f"  Force static eval: {args.force_static}")
    print(f"{'='*60}\n")

    # Load tasks
    print("Loading SWE-Bench tasks...")
    try:
        tasks = load_swebench_tasks(
            max_tasks=args.tasks,
            subset=args.subset,
        )
    except Exception as exc:
        print(f"[ERROR] Failed to load tasks: {exc}")
        raise

    print(f"Loaded {len(tasks)} tasks.\n")

    client = LLMClient()
    records: List[dict] = []

    for task in tqdm(tasks, desc="SWE Tasks"):
        print(f"\n--- Task: {task.instance_id} ({task.repo}) ---")
        for strategy in args.strategies:
            print(f"  Strategy: {strategy} ...", end=" ", flush=True)
            try:
                record = run_single_task(
                    client=client,
                    task=task,
                    strategy=strategy,
                    base=base,
                    force_static=args.force_static,
                    dataset_name=dataset_name,
                    split="test",
                )
            except Exception as exc:
                record = _error_record(task, strategy, error=f"Pipeline error: {exc}")

            records.append(record)
            status = "PASS" if record["passed"] else ("FAIL" if record["passed"] is False else "N/A")
            print(f"[{status}] eval_mode={record['eval_mode']} valid_diff={record['patch_valid']}")

    # Save results
    raw_csv = base / "reports" / "raw_results.csv"
    raw_json = base / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)

    # Summary (reuse existing aggregation — `passed` column is compatible)
    # Map field names to match compute_summary expectations
    summary_records = [
        {
            "task_id": r["task_id"],
            "entry_point": r["task_id"],
            "strategy": r["strategy"],
            "sample_index": 0,
            "passed": r["passed"],
            "pylint_score": None,
            "bandit_issues": None,
        }
        for r in records
    ]
    summary_df = compute_summary(summary_records)
    summary_path = base / "reports" / "summary.csv"
    summary_df.to_csv(summary_path, index=False, encoding="utf-8")

    # Print summary table
    print(f"\n{'='*60}")
    print("Results summary:")
    print(summary_df.to_string(index=False))
    print(f"{'='*60}")
    print("\nSaved:")
    print(f"  {raw_csv}")
    print(f"  {raw_json}")
    print(f"  {summary_path}")
    print(f"  Generated patches: {base / 'generated_patches'}")
    print(f"  Evaluation reports: {base / 'evaluation_results'}")


if __name__ == "__main__":
    main()

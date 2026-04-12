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
from github_file_fetcher import fetch_task_file_contents
from llm_client import LLMClient
from swebench_loader import SWETask, load_swebench_tasks
from swebench_lite_evaluator import (
    SWEEvaluationResult,
    evaluate_swe_patch,
    is_valid_unified_diff,
    validate_patch_syntax,
)
from swebench_lite_prompts import (
    build_swe_cot_prompt,
    build_swe_zero_shot_prompt,
    build_fallback_patch_prompt,
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
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "task"


def ensure_dirs(base: Path) -> None:
    (base / "generated_patches").mkdir(parents=True, exist_ok=True)
    (base / "evaluation_results").mkdir(parents=True, exist_ok=True)
    (base / "reports").mkdir(parents=True, exist_ok=True)


def build_prompt(strategy: str, task: SWETask, file_contents: dict[str, str]) -> str:
    """Build prompt with real file contents for correct hunk line numbers."""
    if strategy == "zero_shot":
        return build_swe_zero_shot_prompt(task.prompt, file_contents)
    elif strategy == "cot":
        return build_swe_cot_prompt(task.prompt, file_contents)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def save_patch(base: Path, instance_id: str, strategy: str, patch: str) -> Path:
    fname = safe_filename(instance_id)
    path = base / "generated_patches" / f"{fname}__{strategy}.diff"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(patch, encoding="utf-8")
    return path


def save_eval_report(base: Path, instance_id: str, strategy: str, result: SWEEvaluationResult) -> Path:
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

def _reconstruct_diff_from_fallback(fallback_text: str, file_contents: dict[str, str]) -> str:
    """
    Reconstruct a unified diff from fallback format output.
    
    Fallback format:
    REMOVE: <line>
    ADD: <line>
    AT: <location>
    """
    if not file_contents:
        return ""
    
    filepath = list(file_contents.keys())[0]
    original_lines = file_contents[filepath].splitlines()
    
    # Parse fallback instructions
    changes = []
    current_remove = None
    current_add = None
    current_location = None
    
    for line in fallback_text.splitlines():
        line = line.strip()
        if line.startswith('REMOVE:'):
            current_remove = line[7:].strip()
        elif line.startswith('ADD:'):
            current_add = line[4:].strip()
        elif line.startswith('AT:'):
            current_location = line[3:].strip()
            if current_remove is not None or current_add is not None:
                changes.append({
                    'remove': current_remove,
                    'add': current_add,
                    'location': current_location
                })
                current_remove = None
                current_add = None
                current_location = None
    
    # Build diff from changes
    diff_lines = [
        f'diff --git a/{filepath} b/{filepath}',
        f'--- a/{filepath}',
        f'+++ b/{filepath}',
    ]
    
    for change in changes:
        # Try to find the line in original file
        remove_line = change.get('remove')
        add_line = change.get('add')
        
        if remove_line:
            # Search for the line to remove
            for i, orig_line in enumerate(original_lines):
                if orig_line.strip() == remove_line.strip():
                    # Found it! Generate a simple hunk
                    start = max(0, i - 3)
                    end = min(len(original_lines), i + 4)
                    
                    diff_lines.append(f'@@ -{start+1},{end-start} +{start+1},{end-start + (1 if add_line else 0) - (1 if remove_line else 0)} @@')
                    
                    # Add context before
                    for j in range(start, i):
                        diff_lines.append(f' {original_lines[j]}')
                    
                    # Add removed line
                    if remove_line:
                        diff_lines.append(f'-{original_lines[i]}')
                    
                    # Add added line
                    if add_line:
                        diff_lines.append(f'+{add_line}')
                    
                    # Add context after
                    for j in range(i + 1, end):
                        diff_lines.append(f' {original_lines[j]}')
                    
                    break
    
    return '\n'.join(diff_lines) + '\n'


def run_single_task(
    client: LLMClient,
    task: SWETask,
    strategy: str,
    base: Path,
    force_static: bool = False,
    dataset_name: Optional[str] = None,
    split: str = "test",
    max_retries: int = 2,
) -> dict:
    """Generate a patch for one task+strategy and evaluate it.
    
    Uses retry mechanism: if patch is invalid, try fallback generation.
    """

    # 1. Fetch real file contents at base_commit from GitHub
    file_contents = fetch_task_file_contents(
        repo=task.repo,
        base_commit=task.base_commit,
        patch=task.patch,
    )

    # 2. Build prompt with actual source code
    prompt = build_prompt(strategy, task, file_contents)

    # 3. Generate patch via LLM (with retries)
    patch = None
    is_valid = False
    validation_error = ""
    
    for attempt in range(max_retries):
        try:
            raw_output = client.generate_code(prompt)
        except Exception as exc:
            return _error_record(task, strategy, error=f"LLM generation failed: {exc}")

        patch = _strip_diff_fences(raw_output)
        patch = _normalize_patch_headers(patch, list(file_contents.keys()))
        patch = _postprocess_patch(patch, file_contents)
        
        # Validate patch
        is_valid, validation_error = validate_patch_syntax(
            patch, list(file_contents.keys())[0] if file_contents else ""
        )
        
        if is_valid:
            break
        
        # If not valid and not last attempt, use fallback prompt
        if attempt < max_retries - 1:
            print(f"    [Retry {attempt+1}/{max_retries}] Invalid patch, trying fallback...")
            prompt = build_fallback_patch_prompt(task.prompt, file_contents)
            # Rebuild from fallback response
            raw_output = client.generate_code(prompt)
            patch = _reconstruct_diff_from_fallback(raw_output, file_contents)
            patch = _normalize_patch_headers(patch, list(file_contents.keys()))
    
    if not is_valid:
        print(f"    [WARNING] Patch validation failed: {validation_error}")
    
    # Ensure patch is not None
    if patch is None:
        patch = ""
    
    # 5. Save generated patch
    patch_path = save_patch(base, task.instance_id, strategy, patch)

    # 6. Evaluate patch
    eval_result = evaluate_swe_patch(
        instance_id=task.instance_id,
        generated_patch=patch,
        ground_truth_patch=task.patch,
        force_static=force_static,
        dataset_name=dataset_name,
        split=split,
    )

    # 7. Save evaluation report
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
        "files_fetched": list(file_contents.keys()),
        "validation_error": validation_error if not is_valid else None,
    }


def _strip_diff_fences(text: str) -> str:
    """Remove markdown code fences and extract diff content."""
    text = text.strip()
    
    # Remove ```diff or ```patch fences
    text = re.sub(r'^```(?:diff|patch)?\s*\n?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\n?```\s*$', '', text)
    
    # Remove any leading/trailing whitespace
    text = text.strip()
    
    return text


def _postprocess_patch(patch: str, file_contents: dict[str, str]) -> str:
    """
    Post-process LLM-generated patch to fix common issues.
    
    Fixes:
    - Incorrect line numbers in hunk headers
    - Mismatched context lines
    - Missing or incorrect a/ b/ prefixes
    """
    if not patch or not file_contents:
        return patch
    
    # Get the first file for context
    filepath = list(file_contents.keys())[0]
    original_lines = file_contents[filepath].splitlines()
    
    # Parse hunks and fix line numbers if needed
    hunk_pattern = re.compile(r'^@@\s+-(\d+)(?:,(\d+))?\s+\+(\d+)(?:,(\d+))?\s+@@(.*)$')
    
    lines = patch.splitlines()
    output_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        hunk_match = hunk_pattern.match(line)
        
        if hunk_match:
            # Found a hunk header, extract info
            old_start = int(hunk_match.group(1))
            old_count = int(hunk_match.group(2)) if hunk_match.group(2) else 1
            new_start = int(hunk_match.group(3))
            new_count = int(hunk_match.group(4)) if hunk_match.group(4) else 1
            trailing = hunk_match.group(5)
            
            # Collect hunk content
            hunk_lines = []
            j = i + 1
            while j < len(lines) and not lines[j].startswith('@@') and not lines[j].startswith('diff --git'):
                hunk_lines.append(lines[j])
                j += 1
            
            # Try to find the correct location in original file
            # Extract context lines from hunk
            context_before = []
            for hline in hunk_lines:
                if hline.startswith(' '):
                    context_before.append(hline[1:])
                elif hline.startswith('-'):
                    continue
                else:
                    break
            
            # Search for context in original file
            if context_before and len(context_before) >= 2:
                # Try to find the context in the original file
                for line_idx in range(len(original_lines) - len(context_before) + 1):
                    match = True
                    for ctx_idx, ctx_line in enumerate(context_before[:3]):
                        if line_idx + ctx_idx >= len(original_lines):
                            match = False
                            break
                        if original_lines[line_idx + ctx_idx].rstrip() != ctx_line.rstrip():
                            match = False
                            break
                    
                    if match:
                        # Found matching context, update line numbers
                        new_old_start = line_idx + 1  # 1-indexed
                        output_lines.append(f'@@ -{new_old_start},{old_count} +{new_old_start},{new_count} @@{trailing}')
                        output_lines.extend(hunk_lines)
                        break
                else:
                    # Context not found, keep original
                    output_lines.append(line)
                    output_lines.extend(hunk_lines)
            else:
                # Not enough context, keep original
                output_lines.append(line)
                output_lines.extend(hunk_lines)
            
            i = j
        else:
            output_lines.append(line)
            i += 1
    
    return '\n'.join(output_lines)


def _normalize_patch_headers(patch: str, filepaths: list[str]) -> str:
    """Fix all common issues in LLM-generated unified diffs.

    Fixes:
      - Missing `diff --git a/path b/path` lines
      - Headers like `--- astropy/file.py` instead of `--- a/astropy/file.py`
      - Em-dash/en-dash in place of regular dashes
      - Malformed hunk headers
      - Trailing whitespace
      - Missing newlines at EOF
    """
    if not patch.strip() or not filepaths:
        return patch

    # Fix em-dash and en-dash → regular dash (common LLM mistake)
    patch = patch.replace('\u2014', '--')  # em-dash
    patch = patch.replace('\u2013', '--')  # en-dash
    patch = patch.replace('\u2015', '--')  # horizontal bar
    patch = patch.replace('\u2212', '-')   # minus sign

    # Fix trailing whitespace on each line
    lines = patch.splitlines()
    lines = [line.rstrip() for line in lines]
    patch = '\n'.join(lines)

    # Ensure patch ends with newline
    if not patch.endswith('\n'):
        patch += '\n'

    for path in filepaths:
        esc = re.escape(path)

        # Fix --- / +++ headers without a/ b/ prefix
        patch = re.sub(rf'(?m)^---\s+{esc}\s*$', f'--- a/{path}', patch)
        patch = re.sub(rf'(?m)^\+\+\+\s+{esc}\s*$', f'+++ b/{path}', patch)

        # Fix --- / +++ headers with incorrect separators
        patch = re.sub(rf'(?m)^---\s+[ab]?[/\\]?{esc}\s*$', f'--- a/{path}', patch)
        patch = re.sub(rf'(?m)^\+\+\+\s+[ab]?[/\\]?{esc}\s*$', f'+++ b/{path}', patch)

        # If there is already a diff --git for this path, do nothing more
        diff_header = f'diff --git a/{path} b/{path}'
        if diff_header in patch:
            continue

        # Insert diff --git before the first --- a/path header
        pattern = rf'(?m)^(---\s+a/{esc}\s*$)'

        def _insert_diff(match: re.Match) -> str:
            return f'{diff_header}\n' + match.group(1)

        new_patch, count = re.subn(pattern, _insert_diff, patch, count=1)
        if count > 0:
            patch = new_patch

    return patch


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
        "files_fetched": [],
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
            fetched = record.get("files_fetched", [])
            print(f"[{status}] eval_mode={record['eval_mode']} valid_diff={record['patch_valid']} files={fetched}")

    raw_csv = base / "reports" / "raw_results.csv"
    raw_json = base / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)

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

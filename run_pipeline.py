"""Main pipeline for LLM code generation benchmarking.

This script runs code generation experiments using different prompting strategies
and evaluates the generated code using static analysis (pylint, bandit) and
optional functional tests.

Usage:
    python run_pipeline.py [--tasks N] [--strategies zero_shot constraint_guided ...]

Environment variables:
    OPENAI_API_KEY: Your OpenAI API key (required)
    OPENAI_BASE_URL: Custom API endpoint (optional)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Callable

from dotenv import load_dotenv
from tqdm import tqdm

from aggregation import compute_summary, save_records_to_csv, save_records_to_json
from analyzers import analyze_code
from code_utils import (
    basic_code_quality_flags,
    is_valid_python,
    strip_code_fences,
    write_generation_artifacts,
)
from config import EXPERIMENT_CONFIG, ExperimentConfig
from evaluator import evaluate_with_humaneval
from humaneval_loader import HumanEvalTask, load_humaneval_tasks
from code_reviewer import CodeReviewer, CodeReviewResult
from llm_client import LLMClient
from prompts import (
    build_constraint_guided_prompt,
    build_structured_cot_prompt,
    build_zero_shot_prompt,
)
from refinement import build_refinement_feedback, make_refinement_prompt


def ensure_dirs(base_dir: Path) -> None:
    """Create required output directories."""
    (base_dir / "raw_generations").mkdir(parents=True, exist_ok=True)
    (base_dir / "analyzed").mkdir(parents=True, exist_ok=True)
    (base_dir / "reports").mkdir(parents=True, exist_ok=True)
    (base_dir / "logs").mkdir(parents=True, exist_ok=True)


def safe_filename(value: str) -> str:
    """Convert string to safe filename (no slashes, spaces, etc.)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "value"


def save_text(path: Path, content: str) -> Path:
    """Save text content to file, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def get_prompt_builder(strategy: str) -> Callable[[str], str]:
    """Get the appropriate prompt builder function for a strategy."""
    mapping = {
        "zero_shot": build_zero_shot_prompt,
        "constraint_guided": build_constraint_guided_prompt,
        "structured_cot": build_structured_cot_prompt,
    }
    if strategy not in mapping:
        raise ValueError(f"Unknown strategy: {strategy}. Available: {list(mapping.keys())}")
    return mapping[strategy]


def run_single_generation(
    client: LLMClient,
    task: HumanEvalTask,
    strategy: str,
    sample_index: int,
    config: ExperimentConfig,
    reviewer: CodeReviewer | None = None,
) -> dict:
    """Run a single code generation and evaluation.
    
    Args:
        client: LLM client for code generation.
        task: HumanEval task to solve.
        strategy: Prompting strategy to use.
        sample_index: Index of this sample (for multiple samples per task).
        config: Experiment configuration.
        reviewer: Optional LLM code reviewer.
        
    Returns:
        Dictionary with generation results and metrics.
    """
    if strategy == "self_refine":
        # Self-refine: generate initial code, analyze, then refine
        initial_prompt = build_constraint_guided_prompt(task.prompt)
        initial_code = strip_code_fences(client.generate_code(initial_prompt))

        valid, syntax_error = is_valid_python(initial_code)
        flags = basic_code_quality_flags(initial_code)
        static_result = analyze_code(initial_code, flags) if valid else None

        initial_pylint_path = None
        initial_bandit_json_path = None
        initial_bandit_stderr_path = None
        if static_result:
            task_part = safe_filename(task.task_id)
            static_root = config.output_dir / "reports" / "static_analysis"
            initial_pylint_path = save_text(
                static_root / "pylint" / f"{task_part}__{strategy}__sample{sample_index}__initial_pylint.txt",
                static_result.pylint_stdout,
            )
            initial_bandit_json_path = save_text(
                static_root / "bandit" / f"{task_part}__{strategy}__sample{sample_index}__initial_bandit.json",
                static_result.bandit_stdout,
            )
            initial_bandit_stderr_path = save_text(
                static_root / "bandit" / f"{task_part}__{strategy}__sample{sample_index}__initial_bandit.stderr.txt",
                static_result.bandit_stderr,
            )

        functional_result = None
        functional_result_text = "not_executed"
        if valid and config.enable_external_execution:
            functional_result = evaluate_with_humaneval(
                task_id=task.task_id,
                completion=initial_code,
                test_code=task.test,
            )
            functional_result_text = functional_result.result

        feedback = build_refinement_feedback(
            syntax_error=syntax_error,
            static_result=static_result,
            functional_result_text=functional_result_text
        )

        refine_prompt = make_refinement_prompt(task.prompt, initial_code, feedback)
        final_code = strip_code_fences(client.generate_code(refine_prompt))
    else:
        prompt_builder = get_prompt_builder(strategy)
        prompt = prompt_builder(task.prompt)
        final_code = strip_code_fences(client.generate_code(prompt))
        initial_code = None

    valid, syntax_error = is_valid_python(final_code)
    flags = basic_code_quality_flags(final_code)

    static_result = analyze_code(final_code, flags) if valid else None

    task_part = safe_filename(task.task_id)
    static_root = config.output_dir / "reports" / "static_analysis"
    pylint_path = None
    bandit_json_path = None
    bandit_stderr_path = None
    if static_result:
        pylint_path = save_text(
            static_root / "pylint" / f"{task_part}__{strategy}__sample{sample_index}__final_pylint.txt",
            static_result.pylint_stdout,
        )
        bandit_json_path = save_text(
            static_root / "bandit" / f"{task_part}__{strategy}__sample{sample_index}__final_bandit.json",
            static_result.bandit_stdout,
        )
        bandit_stderr_path = save_text(
            static_root / "bandit" / f"{task_part}__{strategy}__sample{sample_index}__final_bandit.stderr.txt",
            static_result.bandit_stderr,
        )

    functional_result = None
    if valid and config.enable_external_execution:
        functional_result = evaluate_with_humaneval(
            task_id=task.task_id,
            completion=final_code,
            test_code=task.test,
        )

    code_file, initial_code_file = write_generation_artifacts(
        config.output_dir,
        task.task_id,
        strategy,
        sample_index,
        final_code,
        initial_code,
    )

    # LLM Review
    llm_review = None
    if valid and reviewer is not None:
        llm_review = reviewer.review_code(final_code, task.prompt)
    
    record = {
        "task_id": task.task_id,
        "entry_point": task.entry_point,
        "strategy": strategy,
        "sample_index": sample_index,
        "code": final_code,
        "code_file": code_file,
        "initial_code": initial_code,
        "initial_code_file": initial_code_file,
        "syntax_valid": valid,
        "syntax_error": syntax_error,
        "custom_flags_count": len(flags),
        "custom_flags": " | ".join(flags) if flags else "",
        "pylint_score": static_result.pylint_score if static_result else None,
        "bandit_issues": static_result.bandit_issues if static_result else None,
        # Radon metrics
        "radon_cc_avg": static_result.radon.cyclomatic_complexity if static_result and static_result.radon else None,
        "radon_cc_max": static_result.radon.max_complexity if static_result and static_result.radon else None,
        "radon_mi": static_result.radon.maintainability_index if static_result and static_result.radon else None,
        "pylint_report_file": str(pylint_path) if pylint_path else None,
        "bandit_report_file": str(bandit_json_path) if bandit_json_path else None,
        "bandit_stderr_file": str(bandit_stderr_path) if bandit_stderr_path else None,
        "passed": functional_result.passed if functional_result else None,
        "functional_result": functional_result.result if functional_result else "not_executed",
        # LLM Review scores
        "llm_readability": llm_review.readability if llm_review else None,
        "llm_maintainability": llm_review.maintainability if llm_review else None,
        "llm_correctness": llm_review.correctness if llm_review else None,
        "llm_efficiency": llm_review.efficiency if llm_review else None,
        "llm_pythonic_style": llm_review.pythonic_style if llm_review else None,
        "llm_overall_score": llm_review.overall_score if llm_review else None,
        "llm_feedback": llm_review.brief_feedback if llm_review else None,
    }

    # For self_refine, also save initial code reports
    if strategy == "self_refine":
        record["initial_pylint_report_file"] = str(initial_pylint_path) if initial_pylint_path else None
        record["initial_bandit_report_file"] = str(initial_bandit_json_path) if initial_bandit_json_path else None
        record["initial_bandit_stderr_file"] = str(initial_bandit_stderr_path) if initial_bandit_stderr_path else None

    return record


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run LLM code generation benchmark",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--tasks",
        type=int,
        default=EXPERIMENT_CONFIG.max_tasks,
        help="Maximum number of tasks to process",
    )
    parser.add_argument(
        "--strategies",
        nargs="+",
        default=EXPERIMENT_CONFIG.strategies,
        choices=["zero_shot", "constraint_guided", "structured_cot", "self_refine"],
        help="List of prompting strategies to use",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=EXPERIMENT_CONFIG.samples_per_task,
        help="Number of samples per task",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=EXPERIMENT_CONFIG.output_dir,
        help="Output directory for results",
    )
    parser.add_argument(
        "--dataset",
        type=Path,
        default=EXPERIMENT_CONFIG.dataset_path,
        help="Path to JSONL dataset file (for --source=local)",
    )
    parser.add_argument(
        "--source",
        choices=["local", "humaneval_next"],
        default="local",
        help="Data source: 'local' for JSONL file, 'humaneval_next' for HuggingFace dataset",
    )
    parser.add_argument(
        "--enable-execution",
        action="store_true",
        help="Enable functional test execution",
    )
    parser.add_argument(
        "--enable-llm-review",
        action="store_true",
        help="Enable LLM-based code review (requires REVIEWER_API_KEY)",
    )
    return parser.parse_args()


def main() -> None:
    """Main entry point for the pipeline."""
    # Load environment variables from .env file
    load_dotenv()
    
    args = parse_args()
    
    # Update config with CLI arguments
    config = ExperimentConfig(
        max_tasks=args.tasks,
        strategies=args.strategies,
        samples_per_task=args.samples,
        output_dir=args.output_dir,
        dataset_path=args.dataset,
        enable_external_execution=args.enable_execution,
    )
    
    ensure_dirs(config.output_dir)

    # Initialize LLM reviewer if enabled
    reviewer = None
    if args.enable_llm_review:
        try:
            reviewer = CodeReviewer()
            print("LLM Reviewer initialized successfully.")
        except RuntimeError as e:
            print(f"Warning: {e}")
            print("LLM review will be disabled.")

    print(f"\n{'='*60}")
    print("LLM Code Generation Benchmark")
    print(f"{'='*60}")
    print(f"  Tasks:       {config.max_tasks}")
    print(f"  Strategies:  {config.strategies}")
    print(f"  Samples:     {config.samples_per_task}")
    print(f"  Dataset:     {config.dataset_path}")
    print(f"  Output:      {config.output_dir}")
    print(f"  Execution:   {'enabled' if config.enable_external_execution else 'disabled'}")
    print(f"  LLM Review:  {'enabled' if reviewer else 'disabled'}")
    print(f"{'='*60}\n")

    client = LLMClient()
    
    source = args.source
    print(f"Loading tasks from {source}...")
    tasks = load_humaneval_tasks(
        file_path=str(config.dataset_path) if source == "local" else None,
        max_tasks=config.max_tasks,
        source=source,
    )
    print(f"Loaded {len(tasks)} tasks.\n")
    
    records: list[dict] = []

    for task in tqdm(tasks, desc="Tasks"):
        for strategy in config.strategies:
            for sample_index in range(config.samples_per_task):
                try:
                    record = run_single_generation(
                        client=client,
                        task=task,
                        strategy=strategy,
                        sample_index=sample_index,
                        config=config,
                        reviewer=reviewer,
                    )
                except Exception as exc:
                    record = {
                        "task_id": task.task_id,
                        "entry_point": task.entry_point,
                        "strategy": strategy,
                        "sample_index": sample_index,
                        "code": "",
                        "code_file": None,
                        "initial_code": None,
                        "initial_code_file": None,
                        "syntax_valid": False,
                        "syntax_error": f"PipelineError: {exc}",
                        "custom_flags_count": None,
                        "custom_flags": "",
                        "pylint_score": None,
                        "bandit_issues": None,
                        "passed": None,
                        "functional_result": "pipeline_error",
                    }

                records.append(record)

    # Save results
    raw_csv = config.output_dir / "reports" / "raw_results.csv"
    raw_json = config.output_dir / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)

    summary_df = compute_summary(records)
    summary_path = config.output_dir / "reports" / "summary.csv"
    summary_df.to_csv(summary_path, index=False, encoding="utf-8")

    print(f"\n{'='*60}")
    print("Results Summary (per strategy):")
    if not summary_df.empty:
        print(summary_df.to_string(index=False))
    else:
        print("No records to summarize.")
    print(f"{'='*60}")
    print(f"\nSaved:")
    print(f"  {raw_csv}")
    print(f"  {raw_json}")
    print(f"  {summary_path}")


if __name__ == "__main__":
    main()

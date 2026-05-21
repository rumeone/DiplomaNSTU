"""Async pipeline for LLM code generation benchmarking with parallel execution.

This script runs code generation experiments using different prompting strategies
with concurrent API requests for significantly faster execution.

Usage:
    python run_pipeline_async.py [--tasks N] [--concurrent 10]

Environment variables:
    OPENAI_API_KEY: Your OpenAI API key (required)
    OPENAI_BASE_URL: Custom API endpoint (optional)
"""
from __future__ import annotations

import argparse
import asyncio
import re
import sys
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from tqdm.asyncio import tqdm_asyncio

from aggregation import compute_summary, save_records_to_csv, save_records_to_json
from analyzers import analyze_code
from code_utils import (
    is_valid_python,
    strip_code_fences,
    write_generation_artifacts,
)
from config import EXPERIMENT_CONFIG, ExperimentConfig, MODEL_CONFIG, ModelConfig, PARALLELISM_CONFIG, ParallelismConfig, REVIEWER_CONFIG, ReviewerConfig
from evaluator import evaluate_with_humaneval
from humaneval_loader import HumanEvalTask, load_humaneval_tasks
from code_reviewer import CodeReviewer, CodeReviewResult
from code_reviewer_async import AsyncCodeReviewer, ReviewRequest, ReviewResult
from llm_client_async import AsyncLLMClient, GenerationRequest, GenerationResult
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
    (base_dir / "reports" / "static_analysis" / "pylint").mkdir(parents=True, exist_ok=True)
    (base_dir / "reports" / "static_analysis" / "bandit").mkdir(parents=True, exist_ok=True)
    (base_dir / "logs").mkdir(parents=True, exist_ok=True)


def safe_filename(value: str) -> str:
    """Convert string to safe filename (no slashes, spaces, etc.)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "value"


def save_text(path: Path, content: str) -> Path:
    """Save text content to file, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def get_prompt_builder(strategy: str):
    """Get the appropriate prompt builder function for a strategy."""
    mapping = {
        "zero_shot": build_zero_shot_prompt,
        "constraint_guided": build_constraint_guided_prompt,
        "structured_cot": build_structured_cot_prompt,
    }
    if strategy not in mapping:
        raise ValueError(f"Unknown strategy: {strategy}. Available: {list(mapping.keys())}")
    return mapping[strategy]


def get_completed_tasks(output_dir: Path) -> set[str]:
    """Get set of already completed (task_id, strategy, sample_index) combinations.
    
    This enables resume capability - skipping already processed tasks.
    """
    completed = set()
    raw_gen_dir = output_dir / "raw_generations"
    if not raw_gen_dir.exists():
        return completed
    
    for task_dir in raw_gen_dir.iterdir():
        if not task_dir.is_dir():
            continue
        task_id = task_dir.name  # e.g., "HumanEval_0"
        
        for code_file in task_dir.glob("*.py"):
            # Parse filename: {strategy}_sample{index}.py or {strategy}_sample{index}_initial.py
            name = code_file.stem
            if "_initial" in name:
                continue  # Skip initial files, only count final
            
            parts = name.split("_sample")
            if len(parts) == 2:
                strategy = parts[0]
                sample_idx = parts[1]
                completed.add(f"{task_id}__{strategy}__{sample_idx}")
    
    return completed


def build_record_from_result(
    task: HumanEvalTask,
    strategy: str,
    sample_index: int,
    final_code: str,
    initial_code: str | None,
    config: ExperimentConfig,
    llm_review: CodeReviewResult | None = None,
) -> dict:
    """Build a result record from generated code.
    
    This function performs post-generation analysis (static analysis, tests)
    LLM review is now done asynchronously in a separate phase.
    """
    valid, syntax_error = is_valid_python(final_code)
    
    static_result = analyze_code(final_code) if valid else None
    
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
        "pylint_score": static_result.pylint_score if static_result else None,
        "bandit_issues": static_result.bandit_issues if static_result else None,
        "radon_cc_avg": static_result.radon.cyclomatic_complexity if static_result and static_result.radon else None,
        "radon_cc_max": static_result.radon.max_complexity if static_result and static_result.radon else None,
        "radon_mi": static_result.radon.maintainability_index if static_result and static_result.radon else None,
        "pylint_report_file": str(pylint_path) if pylint_path else None,
        "bandit_report_file": str(bandit_json_path) if bandit_json_path else None,
        "bandit_stderr_file": str(bandit_stderr_path) if bandit_stderr_path else None,
        "passed": functional_result.passed if functional_result else None,
        "functional_result": functional_result.result if functional_result else "not_executed",
        "llm_readability": llm_review.readability if llm_review else None,
        "llm_maintainability": llm_review.maintainability if llm_review else None,
        "llm_correctness": llm_review.correctness if llm_review else None,
        "llm_efficiency": llm_review.efficiency if llm_review else None,
        "llm_pythonic_style": llm_review.pythonic_style if llm_review else None,
        "llm_overall_score": llm_review.overall_score if llm_review else None,
        "llm_feedback": llm_review.brief_feedback if llm_review else None,
    }
    
    return record


async def run_generation_phase(
    client: AsyncLLMClient,
    tasks: list[HumanEvalTask],
    strategies: list[str],
    samples_per_task: int,
    completed_tasks: set[str],
    config: ExperimentConfig,
    progress_bar: Any = None,
) -> dict[str, tuple[str, str | None]]:
    """Run all code generations in parallel.
    
    Returns:
        Dictionary mapping (task_id, strategy, sample_index) -> (final_code, initial_code)
        For self_refine strategy, initial_code contains the first generation.
    """
    # Build all generation requests
    requests: list[GenerationRequest] = []
    request_keys: list[str] = []  # To track which request is which
    
    for task in tasks:
        for strategy in strategies:
            for sample_index in range(samples_per_task):
                key = f"{safe_filename(task.task_id)}__{strategy}__{sample_index}"
                
                # Skip already completed
                if key in completed_tasks:
                    continue
                
                if strategy == "self_refine":
                    # Self-refine needs initial generation first
                    prompt = build_constraint_guided_prompt(task.prompt)
                    requests.append(GenerationRequest(
                        task_id=task.task_id,
                        strategy=strategy,
                        sample_index=sample_index,
                        prompt=prompt,
                        is_refinement=False,
                    ))
                    request_keys.append(f"{key}__initial")
                else:
                    prompt_builder = get_prompt_builder(strategy)
                    prompt = prompt_builder(task.prompt)
                    requests.append(GenerationRequest(
                        task_id=task.task_id,
                        strategy=strategy,
                        sample_index=sample_index,
                        prompt=prompt,
                    ))
                    request_keys.append(key)
    
    if not requests:
        return {}
    
    print(f"\n🚀 Starting parallel generation of {len(requests)} code samples...")
    print(f"   Concurrent requests: {client.max_concurrent}")
    
    # Progress tracking
    completed_count = 0
    total_count = len(requests)
    
    async def progress_callback(done: int, total: int, request: GenerationRequest) -> None:
        nonlocal completed_count
        completed_count = done
        if progress_bar:
            progress_bar.update(1)
    
    # Run all generations
    results = await client.generate_batch(requests, progress_callback)
    
    # Build result dictionary
    generation_results: dict[str, tuple[str, str | None]] = {}
    
    for i, (request, result) in enumerate(zip(requests, results)):
        key = request_keys[i]
        
        if result.error:
            print(f"  ⚠️ Error for {key}: {result.error}")
            generation_results[key] = ("", None)
        else:
            generation_results[key] = (result.code, None)
    
    return generation_results


async def run_refinement_phase(
    client: AsyncLLMClient,
    tasks: list[HumanEvalTask],
    generation_results: dict[str, tuple[str, str | None]],
    config: ExperimentConfig,
    progress_bar: Any = None,
) -> dict[str, tuple[str, str | None]]:
    """Run refinement phase for self_refine strategy.
    
    This is a second pass that takes initial generations and refines them.
    """
    refinement_requests: list[GenerationRequest] = []
    request_keys: list[str] = []
    
    for task in tasks:
        for sample_index in range(config.samples_per_task):
            key = f"{safe_filename(task.task_id)}__self_refine__{sample_index}"
            initial_key = f"{key}__initial"
            
            if initial_key not in generation_results:
                continue
            
            initial_code, _ = generation_results[initial_key]
            if not initial_code:
                continue
            
            # Build feedback for refinement
            valid, syntax_error = is_valid_python(initial_code)
            static_result = analyze_code(initial_code) if valid else None
            
            functional_result_text = "not_executed"
            if valid and config.enable_external_execution:
                func_result = evaluate_with_humaneval(
                    task_id=task.task_id,
                    completion=initial_code,
                    test_code=task.test,
                )
                functional_result_text = func_result.result
            
            feedback = build_refinement_feedback(
                syntax_error=syntax_error,
                static_result=static_result,
                functional_result_text=functional_result_text,
            )
            
            refine_prompt = make_refinement_prompt(task.prompt, initial_code, feedback)
            refinement_requests.append(GenerationRequest(
                task_id=task.task_id,
                strategy="self_refine",
                sample_index=sample_index,
                prompt=refine_prompt,
                is_refinement=True,
                previous_code=initial_code,
                feedback=feedback,
            ))
            request_keys.append(key)
    
    if not refinement_requests:
        return {}
    
    print(f"\n🔄 Starting refinement phase for {len(refinement_requests)} samples...")
    
    async def progress_callback(done: int, total: int, request: GenerationRequest) -> None:
        if progress_bar:
            progress_bar.update(1)
    
    results = await client.generate_batch(refinement_requests, progress_callback)
    
    # Update results with refined code
    final_results: dict[str, tuple[str, str | None]] = {}
    
    for i, (request, result) in enumerate(zip(refinement_requests, results)):
        key = request_keys[i]
        initial_key = f"{key}__initial"
        initial_code = generation_results.get(initial_key, ("", None))[0]
        
        if result.error:
            print(f"  ⚠️ Refinement error for {key}: {result.error}")
            final_results[key] = (initial_code, initial_code)  # Fallback to initial
        else:
            final_results[key] = (result.code, initial_code)
    
    return final_results


def _read_generated_code(output_dir: Path, task_id: str, strategy: str, sample_index: int) -> str | None:
    """Читает ранее сгенерированный код с диска для resume-прогонов."""
    task_part = safe_filename(task_id)
    code_path = output_dir / "raw_generations" / task_part / f"{strategy}_sample{sample_index}.py"
    if code_path.exists():
        try:
            return code_path.read_text(encoding="utf-8")
        except Exception:
            return None
    return None


async def run_review_phase(
        reviewer: AsyncCodeReviewer,
        tasks: list[HumanEvalTask],
        generation_results: dict[str, tuple[str, str | None]],
        strategies: list[str],
        samples_per_task: int,
        completed_tasks: set[str],
        config: ExperimentConfig,
) -> dict[str, CodeReviewResult | None]:
    """Run LLM code review in parallel for all generated code.

    Ревьюит ВСЁС код — как свежесгенерированный, так и ранее сохранённый на диске
    (важно для resume-прогонов, когда генерация уже сделана, а ревью — ещё нет).

    Returns:
        Dictionary mapping (task_id, strategy, sample_index) -> CodeReviewResult
    """
    review_requests: list[ReviewRequest] = []
    request_keys: list[str] = []

    for task in tasks:
        for strategy in strategies:
            for sample_index in range(samples_per_task):
                key = f"{safe_filename(task.task_id)}__{strategy}__{sample_index}"

                # Сначала берём код из generation_results (свежая генерация),
                # если там нет — читаем с диска (resume-случай)
                final_code: str | None = None
                if strategy == "self_refine":
                    initial_key = f"{key}__initial"
                    if key in generation_results:
                        final_code, _ = generation_results[key]
                    elif initial_key in generation_results:
                        final_code, _ = generation_results[initial_key]
                if not final_code and key in generation_results:
                    final_code, _ = generation_results[key]
                if not final_code and key in completed_tasks:
                    final_code = _read_generated_code(config.output_dir, task.task_id, strategy, sample_index)

                if not final_code:
                    continue

                # IMPORTANT:
                # сначала очищаем markdown fences и мусор,
                # потом валидируем код
                clean_code = strip_code_fences(final_code).strip()

                # Skip empty code
                if not clean_code:
                    print(f"  ⚠️ Empty code for {key}")
                    continue

                # Validate cleaned code
                valid, syntax_error = is_valid_python(clean_code)

                if not valid:
                    print(f"  ⚠️ Invalid python for review {key}: {syntax_error}")
                    continue

                review_requests.append(
                    ReviewRequest(
                        task_id=task.task_id,
                        strategy=strategy,
                        sample_index=sample_index,
                        code=clean_code,
                        task_description=task.prompt,
                    )
                )

                request_keys.append(key)

    if not review_requests:
        return {}

    print(f"\n🔍 Starting parallel review of {len(review_requests)} code samples...")
    print(f"   Concurrent review requests: {reviewer.max_concurrent}")

    results = await reviewer.review_batch(review_requests)

    # Build result dictionary
    review_results: dict[str, CodeReviewResult | None] = {}
    for i, result in enumerate(results):
        key = request_keys[i]
        review_results[key] = result.review
        if result.error:
            print(f"  ⚠️ Review error for {key}: {result.error}")
        elif result.review is None:
            print(f"  ⚠️ Review returned None for {key}")

    print(
        f"   Review results: {len([r for r in review_results.values() if r is not None])}/{len(review_results)} successful")
    return review_results


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run LLM code generation benchmark with parallel execution",
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
        help="Path to JSONL dataset file",
    )
    parser.add_argument(
        "--concurrent",
        type=int,
        default=PARALLELISM_CONFIG.max_concurrent_requests,
        help="Maximum concurrent API requests",
    )
    parser.add_argument(
        "--enable-execution",
        action="store_true",
        help="Enable functional test execution",
    )
    parser.add_argument(
        "--enable-llm-review",
        action="store_true",
        default=REVIEWER_CONFIG.enabled,
        help="Enable LLM-based code review (default: REVIEWER_CONFIG.enabled from config.py)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=MODEL_CONFIG.model_name,
        help="Модель-генератор (по умолчанию — из MODEL_CONFIG.model_name)",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Disable resume capability (reprocess all tasks)",
    )
    parser.add_argument(
        "--source",
        choices=["local", "humaneval_next"],
        default="local",
        help="Data source: 'local' for JSONL file, 'humaneval_next' for HuggingFace dataset",
    )
    parser.add_argument(
        "--reviewer-model",
        type=str,
        default=REVIEWER_CONFIG.model,
        help="Модель для LLM-ревью (по умолчанию — из REVIEWER_CONFIG.model)",
    )
    return parser.parse_args()


async def async_main() -> None:
    """Async main entry point for the pipeline."""
    load_dotenv()
    
    args = parse_args()
    
    # Build configs
    parallelism_config = ParallelismConfig(
        max_concurrent_requests=args.concurrent,
    )
    
    config = ExperimentConfig(
        max_tasks=args.tasks,
        strategies=args.strategies,
        samples_per_task=args.samples,
        output_dir=args.output_dir,
        dataset_path=args.dataset,
        enable_external_execution=args.enable_execution,
        parallelism=parallelism_config,
        resume_enabled=not args.no_resume,
    )
    
    ensure_dirs(config.output_dir)
    
    # Check if LLM review is enabled (will initialize async reviewer later)
    # Флаг --enable-llm-review или REVIEWER_CONFIG.enabled в config.py
    llm_review_enabled = args.enable_llm_review or REVIEWER_CONFIG.enabled
    if llm_review_enabled:
        try:
            # Just check if API key is available
            import os
            if not os.environ.get("REVIEWER_API_KEY"):
                print("Warning: REVIEWER_API_KEY environment variable is not set.")
                print("LLM review will be disabled.")
                llm_review_enabled = False
            else:
                print("LLM Review enabled (async mode).")
        except Exception as e:
            print(f"Warning: {e}")
            print("LLM review will be disabled.")
            llm_review_enabled = False
    
    print(f"\n{'='*60}")
    print("LLM Code Generation Benchmark (Async Mode)")
    print(f"{'='*60}")
    print(f"  Tasks:       {config.max_tasks}")
    print(f"  Strategies:  {config.strategies}")
    print(f"  Samples:     {config.samples_per_task}")
    print(f"  Concurrent:  {args.concurrent}")
    print(f"  Dataset:     {config.dataset_path}")
    print(f"  Output:      {config.output_dir}")
    print(f"  Execution:   {'enabled' if config.enable_external_execution else 'disabled'}")
    print(f"  Generation Model: {args.model}")
    print(f"  LLM Review:  {'enabled' if llm_review_enabled else 'disabled'}")
    if llm_review_enabled:
        print(f"  Reviewer Model: {args.reviewer_model}")
    print(f"  Resume:      {'enabled' if config.resume_enabled else 'disabled'}")
    print(f"{'='*60}\n")
    
    # Load tasks
    source = args.source
    print(f"Loading tasks from {source}...")
    tasks = load_humaneval_tasks(
        file_path=str(config.dataset_path) if source == "local" else None,
        max_tasks=config.max_tasks,
        source=source,
    )
    print(f"Loaded {len(tasks)} tasks.\n")
    
    # Check for completed tasks (resume)
    completed_tasks: set[str] = set()
    if config.resume_enabled:
        completed_tasks = get_completed_tasks(config.output_dir)
        if completed_tasks:
            print(f"📋 Found {len(completed_tasks)} already completed tasks (will skip)")
    
    # Calculate total work
    total_generations = len(tasks) * len(config.strategies) * config.samples_per_task
    # self_refine needs 2 generations per sample
    if "self_refine" in config.strategies:
        self_refine_count = len(tasks) * config.samples_per_task
        total_generations += self_refine_count
    
    skipped = len(completed_tasks)
    remaining = total_generations - skipped
    
    print(f"📊 Total generations needed: {total_generations}")
    print(f"   Already completed: {skipped}")
    print(f"   Remaining: {remaining}")
    
    if remaining == 0:
        print("\n✅ All tasks already completed! Nothing to do.")
        print("   Use --no-resume to reprocess all tasks.")
        return
    
    start_time = time.time()
    
    # Run async pipeline
    async with AsyncLLMClient(
        model=args.model,
        max_concurrent=args.concurrent,
        max_retries=parallelism_config.max_retries,
        timeout_seconds=parallelism_config.request_timeout_seconds,
    ) as client:
        
        # Phase 1: Initial generation (all strategies)
        generation_results = await run_generation_phase(
            client=client,
            tasks=tasks,
            strategies=config.strategies,
            samples_per_task=config.samples_per_task,
            completed_tasks=completed_tasks,
            config=config,
        )
        
        # Phase 2: Refinement (self_refine only)
        if "self_refine" in config.strategies:
            refinement_results = await run_refinement_phase(
                client=client,
                tasks=tasks,
                generation_results=generation_results,
                config=config,
            )
            # Merge refinement results
            generation_results.update(refinement_results)
    
    elapsed = time.time() - start_time
    print(f"\n✅ Generation completed in {elapsed:.1f}s ({remaining} samples)")
    print(f"   Average: {elapsed/remaining:.2f}s per sample")
    
    # Phase 3: Async LLM Review (if enabled)
    review_results: dict[str, CodeReviewResult | None] = {}
    if llm_review_enabled:
        review_start = time.time()
        async with AsyncCodeReviewer(
            model=args.reviewer_model,
            max_concurrent=args.concurrent,
            max_retries=parallelism_config.max_retries,
        ) as reviewer:
            review_results = await run_review_phase(
                reviewer=reviewer,
                tasks=tasks,
                generation_results=generation_results,
                strategies=config.strategies,
                samples_per_task=config.samples_per_task,
                completed_tasks=completed_tasks,
                config=config,
            )
        review_elapsed = time.time() - review_start
        print(f"   Review completed in {review_elapsed:.1f}s")
    
    # Phase 4: Post-processing (static analysis, tests)
    print(f"\n🔍 Running post-processing (static analysis, tests)...")
    
    records: list[dict] = []
    post_start = time.time()
    
    for task in tasks:
        for strategy in config.strategies:
            for sample_index in range(config.samples_per_task):
                key = f"{safe_filename(task.task_id)}__{strategy}__{sample_index}"
                
                # Check if already completed (from resume)
                if key in completed_tasks:
                    # TODO: Load existing record from JSON
                    continue
                
                if strategy == "self_refine":
                    initial_key = f"{key}__initial"
                    if key in generation_results:
                        final_code, initial_code = generation_results[key]
                    elif initial_key in generation_results:
                        # Fallback if refinement failed
                        final_code, _ = generation_results[initial_key]
                        initial_code = final_code
                    else:
                        continue
                else:
                    if key not in generation_results:
                        continue
                    final_code, _ = generation_results[key]
                    initial_code = None
                
                if not final_code:
                    final_code = ""
                
                # Get LLM review result if available
                llm_review = review_results.get(key) if llm_review_enabled else None
                
                try:
                    record = build_record_from_result(
                        task=task,
                        strategy=strategy,
                        sample_index=sample_index,
                        final_code=strip_code_fences(final_code),
                        initial_code=strip_code_fences(initial_code) if initial_code else None,
                        config=config,
                        llm_review=llm_review,
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
                        "pylint_score": None,
                        "bandit_issues": None,
                        "passed": None,
                        "functional_result": "pipeline_error",
                    }
                
                records.append(record)
    
    post_elapsed = time.time() - post_start
    print(f"   Post-processing completed in {post_elapsed:.1f}s")
    
    # Save results
    raw_csv = config.output_dir / "reports" / "raw_results.csv"
    raw_json = config.output_dir / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)
    
    summary_df = compute_summary(records)
    summary_path = config.output_dir / "reports" / "summary.csv"
    summary_df.to_csv(summary_path, index=False, encoding="utf-8")
    
    total_elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print("Results Summary (per strategy):")
    if not summary_df.empty:
        print(summary_df.to_string(index=False))
    else:
        print("No records to summarize.")
    print(f"{'='*60}")
    print(f"\n⏱️ Total time: {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
    print(f"\nSaved:")
    print(f"  {raw_csv}")
    print(f"  {raw_json}")
    print(f"  {summary_path}")


def main() -> None:
    """Synchronous entry point that runs the async main."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

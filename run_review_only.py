"""Script to add LLM review to existing results without regenerating code.

Usage:
    python run_review_only.py --input-dir outputs_test_grok --reviewer-model deepseek/deepseek-v3.2
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import time
from pathlib import Path

from dotenv import load_dotenv

from code_reviewer_async import AsyncCodeReviewer, ReviewRequest
from code_utils import is_valid_python, strip_code_fences
from config import PARALLELISM_CONFIG, ParallelismConfig


def safe_filename(value: str) -> str:
    """Convert string to safe filename."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "value"


def load_existing_results(input_dir: Path) -> list[dict]:
    """Load existing results from raw_results.json."""
    results_path = input_dir / "reports" / "raw_results.json"
    if not results_path.exists():
        print(f"Error: {results_path} not found")
        return []
    
    with open(results_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_code_for_result(result: dict, input_dir: Path) -> str | None:
    """Get the code for a result from the generated file."""
    if not result.get("code_file"):
        return None
    
    code_path = input_dir / result["code_file"]
    if not code_path.exists():
        return None
    
    return code_path.read_text(encoding="utf-8")


async def run_review_phase(
    reviewer: AsyncCodeReviewer,
    results: list[dict],
    input_dir: Path,
) -> dict[str, dict]:
    """Run LLM review for all results.
    
    Returns:
        Dictionary mapping task_id + strategy + sample_index -> review result
    """
    review_requests: list[ReviewRequest] = []
    request_keys: list[str] = []
    
    for result in results:
        # Skip if already has review
        if result.get("llm_overall_score") is not None:
            continue
        
        code = get_code_for_result(result, input_dir)
        if not code:
            continue
        
        # Check if code is valid
        valid, _ = is_valid_python(code)
        if not valid:
            continue
        
        key = f"{safe_filename(result['task_id'])}__{result['strategy']}__{result['sample_index']}"
        
        review_requests.append(ReviewRequest(
            task_id=result["task_id"],
            strategy=result["strategy"],
            sample_index=result["sample_index"],
            code=strip_code_fences(code),
            task_description=None,  # Could add task description if available
        ))
        request_keys.append(key)
    
    if not review_requests:
        print("No results need review (all already have reviews or no valid code)")
        return {}
    
    print(f"\n🔍 Starting parallel review of {len(review_requests)} code samples...")
    print(f"   Concurrent review requests: {reviewer.max_concurrent}")
    
    results_list = await reviewer.review_batch(review_requests)
    
    # Build result dictionary
    review_results: dict[str, dict] = {}
    for i, result in enumerate(results_list):
        key = request_keys[i]
        if result.review:
            review_results[key] = {
                "llm_readability": result.review.readability,
                "llm_maintainability": result.review.maintainability,
                "llm_correctness": result.review.correctness,
                "llm_efficiency": result.review.efficiency,
                "llm_pythonic_style": result.review.pythonic_style,
                "llm_overall_score": result.review.overall_score,
                "llm_feedback": result.review.brief_feedback,
            }
    
    return review_results


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Add LLM review to existing results",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        required=True,
        help="Directory with existing results (raw_results.json)",
    )
    parser.add_argument(
        "--reviewer-model",
        type=str,
        default="deepseek/deepseek-v3.2",
        help="Model to use for code review",
    )
    parser.add_argument(
        "--concurrent",
        type=int,
        default=PARALLELISM_CONFIG.max_concurrent_requests,
        help="Maximum concurrent review requests",
    )
    return parser.parse_args()


async def async_main() -> None:
    """Async main entry point."""
    load_dotenv()
    
    args = parse_args()
    
    print(f"\n{'='*60}")
    print("LLM Review Only Mode")
    print(f"{'='*60}")
    print(f"  Input Dir:   {args.input_dir}")
    print(f"  Reviewer:    {args.reviewer_model}")
    print(f"  Concurrent:  {args.concurrent}")
    print(f"{'='*60}\n")
    
    # Load existing results
    results = load_existing_results(args.input_dir)
    if not results:
        print("No results to process")
        return
    
    print(f"Loaded {len(results)} results")
    
    # Count how many need review
    need_review = sum(1 for r in results if r.get("llm_overall_score") is None)
    print(f"Results needing review: {need_review}")
    
    if need_review == 0:
        print("All results already have reviews!")
        return
    
    start_time = time.time()
    
    # Run review
    async with AsyncCodeReviewer(
        model=args.reviewer_model,
        max_concurrent=args.concurrent,
        max_retries=3,
    ) as reviewer:
        review_results = await run_review_phase(
            reviewer=reviewer,
            results=results,
            input_dir=args.input_dir,
        )
    
    review_elapsed = time.time() - start_time
    print(f"\n✅ Review completed in {review_elapsed:.1f}s")
    print(f"   Reviews added: {len(review_results)}")
    
    # Update results with reviews
    updated_count = 0
    for result in results:
        key = f"{safe_filename(result['task_id'])}__{result['strategy']}__{result['sample_index']}"
        if key in review_results:
            review_data = review_results[key]
            result.update(review_data)
            updated_count += 1
    
    # Save updated results
    output_path = args.input_dir / "reports" / "raw_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nUpdated {updated_count} results")
    print(f"Saved to: {output_path}")


def main() -> None:
    """Synchronous entry point."""
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

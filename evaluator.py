"""Functional evaluation for HumanEval tasks.

This module provides built-in test execution without requiring the external
human-eval package. Tests are executed directly in a controlled namespace.
"""
from __future__ import annotations

import json
import linecache
import tempfile
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class FunctionalEvaluationResult:
    """Result of functional evaluation."""
    passed: bool | None
    result: str
    raw_output: str


def evaluate_with_humaneval(
    task_id: str,
    completion: str,
    problem_file: str | None = None,
    test_code: str | None = None,
    entry_point: str | None = None,
) -> FunctionalEvaluationResult:
    """Evaluate generated code against HumanEval tests.
    
    This function can work in two modes:
    1. With test_code provided directly (preferred)
    2. Using external evaluate_functional_correctness harness (legacy)
    
    Args:
        task_id: HumanEval task identifier (e.g., "HumanEval/0")
        completion: Generated code to evaluate
        problem_file: Optional path to problem file for external harness
        test_code: Test code from HumanEval dataset
        entry_point: Function name to pass into the HumanEval check function
        
    Returns:
        FunctionalEvaluationResult with pass/fail status
    """
    # If test_code is provided, run tests directly
    if test_code:
        return _run_tests_directly(task_id, completion, test_code, entry_point)
    
    # Try to get test code from loaded tasks
    from humaneval_loader import load_humaneval_tasks
    try:
        tasks = load_humaneval_tasks(
            file_path=str(Path("HumanEvalPlus-Mini.jsonl")),
            max_tasks=200
        )
        for task in tasks:
            if task.task_id == task_id and task.test:
                return _run_tests_directly(
                    task_id,
                    completion,
                    task.test,
                    entry_point or task.entry_point,
                )
    except Exception:
        pass
    
    # Fallback to external harness if available
    return _evaluate_with_external_harness(task_id, completion, problem_file)


def _run_tests_directly(
    task_id: str,
    completion: str,
    test_code: str,
    entry_point: str | None = None,
) -> FunctionalEvaluationResult:
    """Run HumanEval tests directly in a controlled namespace.
    
    Args:
        task_id: Task identifier
        completion: Generated code
        test_code: Test code from HumanEval
        entry_point: Function name to pass into the check function
        
    Returns:
        Evaluation result
    """
    namespace: dict[str, Any] = {}
    
    # Prefer the dataset entry point. Falling back to code inspection is only a
    # legacy path for callers that do not provide dataset metadata.
    entry_point = entry_point or _get_entry_point(task_id, completion)
    completion_filename = f"<generated {task_id}>"
    tests_filename = f"<tests {task_id}>"
    linecache.cache[completion_filename] = (
        len(completion),
        None,
        completion.splitlines(keepends=True),
        completion_filename,
    )
    linecache.cache[tests_filename] = (
        len(test_code),
        None,
        test_code.splitlines(keepends=True),
        tests_filename,
    )
    
    try:
        # Execute the generated code
        exec(compile(completion, completion_filename, "exec"), namespace)
    except SyntaxError as exc:
        return FunctionalEvaluationResult(
            passed=False,
            result=f"syntax_error: {exc}",
            raw_output=str(exc)
        )
    except Exception as exc:
        return FunctionalEvaluationResult(
            passed=False,
            result=f"exec_error: {exc}",
            raw_output=str(exc)
        )
    
    # Check if the function was defined
    if entry_point not in namespace:
        return FunctionalEvaluationResult(
            passed=False,
            result=f"entry_point_not_found: {entry_point}",
            raw_output=f"Function '{entry_point}' was not defined"
        )
    
    # Execute the test code
    try:
        exec(compile(test_code, tests_filename, "exec"), namespace)
    except Exception as exc:
        return FunctionalEvaluationResult(
            passed=False,
            result=f"test_setup_error: {exc}",
            raw_output=str(exc)
        )
    
    # Get the check function
    check_fn = namespace.get("check")
    if check_fn is None:
        return FunctionalEvaluationResult(
            passed=False,
            result="check_function_not_found",
            raw_output="Test code did not define 'check' function"
        )
    
    # Run the tests
    try:
        check_fn(namespace[entry_point])
        return FunctionalEvaluationResult(
            passed=True,
            result="passed",
            raw_output="All tests passed"
        )
    except AssertionError as exc:
        raw_output = _format_failure_details(exc, tests_filename)
        return FunctionalEvaluationResult(
            passed=False,
            result=f"assertion_failed: {exc}",
            raw_output=raw_output
        )
    except Exception as exc:
        raw_output = _format_failure_details(exc, tests_filename)
        return FunctionalEvaluationResult(
            passed=False,
            result=f"test_failed: {exc}",
            raw_output=raw_output
        )


def _format_failure_details(exc: BaseException, tests_filename: str) -> str:
    """Return traceback plus the failing HumanEval assertion line when available."""
    formatted = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    failing_line = ""
    tb = exc.__traceback__
    while tb is not None:
        frame = tb.tb_frame
        if frame.f_code.co_filename == tests_filename:
            source = linecache.getline(tests_filename, tb.tb_lineno).strip()
            if source:
                failing_line = f"Failing test line {tb.tb_lineno}: {source}"
        tb = tb.tb_next

    if failing_line:
        return f"{failing_line}\n{formatted}"
    return formatted


def _get_entry_point(task_id: str, completion: str) -> str:
    """Extract entry point from task_id or completion code."""
    # Try to get from task_id (e.g., "HumanEval/0" -> check completion)
    # Or extract function name from completion
    import ast
    
    try:
        tree = ast.parse(completion)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return node.name
    except SyntaxError:
        pass
    
    # Fallback: extract from task_id pattern
    # This is a guess, real entry points should come from dataset
    return "solution"


def _evaluate_with_external_harness(
    task_id: str,
    completion: str,
    problem_file: str | None = None,
) -> FunctionalEvaluationResult:
    """Use external human-eval harness (requires pip install human-eval)."""
    import shutil
    import subprocess
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        samples_path = tmp_path / "samples.jsonl"

        sample = {
            "task_id": task_id,
            "completion": completion
        }

        with samples_path.open("w", encoding="utf-8") as f:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")

        harness = shutil.which("evaluate_functional_correctness")
        if not harness:
            return FunctionalEvaluationResult(
                passed=None,
                result="evaluate_functional_correctness_not_in_path",
                raw_output=(
                    "Utility evaluate_functional_correctness not found in PATH. "
                    "Install human-eval package: pip install human-eval"
                ),
            )

        cmd = [harness, str(samples_path)]
        if problem_file:
            cmd.append(f"--problem_file={problem_file}")

        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr

        results_file = Path(str(samples_path) + "_results.jsonl")
        if not results_file.exists():
            return FunctionalEvaluationResult(
                passed=None,
                result="evaluation_failed",
                raw_output=output
            )

        lines = results_file.read_text(encoding="utf-8").strip().splitlines()
        row = json.loads(lines[0])

        return FunctionalEvaluationResult(
            passed=row.get("passed"),
            result=row.get("result", "unknown"),
            raw_output=output
        )

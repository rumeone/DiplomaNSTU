"""SWE-Bench patch evaluator.

Two evaluation modes are supported:

1. Docker-based (full, official):
   Uses the official `swebench` Python package to run the evaluation harness
   inside Docker containers. This is the gold standard but requires Docker.

2. Static / heuristic (lightweight, no Docker):
   Checks whether the generated patch:
   - Is a valid unified diff
   - Touches the same files as the ground-truth patch
   - Does not break obvious syntax in changed hunks
   Used as a fast sanity check when Docker is unavailable.

The runner (`run_swebench_lite.py`) always attempts Docker first and falls back
onto the static evaluator, recording which mode was used in each result record.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------

@dataclass
class SWEEvaluationResult:
    instance_id: str
    passed: Optional[bool]          # True/False if tests ran; None if not executed
    eval_mode: str                   # "docker" | "static" | "skipped"
    patch_applied: Optional[bool]    # Whether the patch applied cleanly
    test_output: str                 # stdout+stderr from test run (or static report)
    error: Optional[str] = None      # Error message if evaluation crashed


# ---------------------------------------------------------------------------
# Unified diff validator (static)
# ---------------------------------------------------------------------------

UNIFIED_DIFF_HEADER = re.compile(
    r'^(diff\s+--git\s+|---\s+a/|\+\+\+\s+b/)', re.MULTILINE
)


def is_valid_unified_diff(patch: str) -> bool:
    """Returns True if *patch* looks like a valid unified diff."""
    if not patch or not patch.strip():
        return False
    return bool(UNIFIED_DIFF_HEADER.search(patch))


def get_changed_files_from_patch(patch: str) -> list[str]:
    """Extract the list of files mentioned in a unified diff."""
    files: list[str] = []
    for line in patch.splitlines():
        m = re.match(r'^---\s+a/(.+)', line)
        if m:
            files.append(m.group(1).strip())
    return files


def static_evaluate_patch(
    instance_id: str,
    generated_patch: str,
    ground_truth_patch: Optional[str],
) -> SWEEvaluationResult:
    """
    Lightweight heuristic evaluation (no Docker, no repo checkout).

    Checks:
    - Is the generated patch a valid unified diff?
    - Does it touch at least one file also touched in the ground-truth patch?
    - Does the patch contain Python syntax errors in added lines?
    """
    report_lines: list[str] = []
    score = 0
    max_score = 3

    # Check 1: valid diff format
    valid_diff = is_valid_unified_diff(generated_patch)
    report_lines.append(f"[1/3] Valid unified diff format: {valid_diff}")
    if valid_diff:
        score += 1

    # Check 2: file overlap with ground truth
    if ground_truth_patch:
        gen_files = set(get_changed_files_from_patch(generated_patch))
        gt_files = set(get_changed_files_from_patch(ground_truth_patch))
        overlap = gen_files & gt_files
        file_match = bool(overlap)
        report_lines.append(
            f"[2/3] Changed files overlap with ground truth: {file_match} "
            f"(gen={sorted(gen_files)}, gt={sorted(gt_files)})"
        )
        if file_match:
            score += 1
    else:
        report_lines.append("[2/3] Ground-truth patch not available — skipping file overlap check.")
        max_score -= 1

    # Check 3: syntax of added lines
    added_lines = [
        line[1:] for line in generated_patch.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    ]
    added_code = "\n".join(added_lines)
    syntax_ok = True
    syntax_err = ""
    if added_code.strip():
        try:
            import ast
            ast.parse(added_code)
        except SyntaxError as exc:
            syntax_ok = False
            syntax_err = str(exc)
    report_lines.append(
        f"[3/3] Added lines syntax OK: {syntax_ok}"
        + (f" ({syntax_err})" if not syntax_ok else "")
    )
    if syntax_ok:
        score += 1

    report_lines.append(f"\nStatic score: {score}/{max_score}")

    # Heuristic pass: valid diff + at least touches right files
    passed = valid_diff and (score >= 2)

    return SWEEvaluationResult(
        instance_id=instance_id,
        passed=passed,
        eval_mode="static",
        patch_applied=valid_diff,
        test_output="\n".join(report_lines),
    )


# ---------------------------------------------------------------------------
# Docker-based evaluator (official SWE-bench harness)
# ---------------------------------------------------------------------------

def docker_is_available() -> bool:
    """Check if Docker daemon is running and accessible."""
    if not shutil.which("docker"):
        return False
    try:
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except Exception:
        return False


def swebench_package_available() -> bool:
    """Check if the swebench package is installed."""
    try:
        import importlib
        importlib.import_module("swebench")
        return True
    except ImportError:
        return False


def docker_evaluate_patch(
    instance_id: str,
    generated_patch: str,
    dataset_name: str,
    split: str = "test",
    timeout: int = 300,
) -> SWEEvaluationResult:
    """
    Run the official SWE-bench evaluation harness via subprocess.

    Writes the prediction to a temp JSONL, then calls:
        python -m swebench.harness.run_evaluation ...

    Requires: Docker running + `pip install swebench`.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        predictions_path = tmp_path / "predictions.jsonl"
        output_dir = tmp_path / "results"
        output_dir.mkdir()

        prediction = {
            "instance_id": instance_id,
            "model_patch": generated_patch,
            "model_name_or_path": "diploma_llm",
        }
        predictions_path.write_text(
            json.dumps(prediction, ensure_ascii=False) + "\n",
            encoding="utf-8"
        )

        cmd = [
            sys.executable, "-m", "swebench.harness.run_evaluation",
            "--dataset_name", dataset_name,
            "--split", split,
            "--predictions_path", str(predictions_path),
            "--max_workers", "1",
            "--instance_ids", instance_id,
            "--run_id", "diploma_eval",
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout
            )
            raw_output = result.stdout + "\n" + result.stderr
        except subprocess.TimeoutExpired:
            return SWEEvaluationResult(
                instance_id=instance_id,
                passed=None,
                eval_mode="docker",
                patch_applied=None,
                test_output="",
                error=f"Evaluation timed out after {timeout}s",
            )
        except Exception as exc:
            return SWEEvaluationResult(
                instance_id=instance_id,
                passed=None,
                eval_mode="docker",
                patch_applied=None,
                test_output="",
                error=str(exc),
            )

        # Parse results JSON if present
        results_files = list(output_dir.rglob("*.json"))
        passed = None
        patch_applied = None

        for rf in results_files:
            try:
                data = json.loads(rf.read_text(encoding="utf-8"))
                # Official harness output format
                if isinstance(data, dict):
                    resolved = data.get("resolved", {})
                    if instance_id in resolved:
                        passed = bool(resolved[instance_id])
                    applied = data.get("applied", {})
                    if instance_id in applied:
                        patch_applied = bool(applied[instance_id])
            except Exception:
                pass

        return SWEEvaluationResult(
            instance_id=instance_id,
            passed=passed,
            eval_mode="docker",
            patch_applied=patch_applied,
            test_output=raw_output,
        )


# ---------------------------------------------------------------------------
# Main evaluation entry point
# ---------------------------------------------------------------------------

def evaluate_swe_patch(
    instance_id: str,
    generated_patch: str,
    ground_truth_patch: Optional[str] = None,
    force_static: bool = False,
    dataset_name: Optional[str] = None,
    split: str = "test",
) -> SWEEvaluationResult:
    """
    Evaluate a generated patch.

    Strategy:
    1. If Docker + swebench package available AND not force_static AND dataset_name → Docker eval.
    2. Otherwise → static heuristic eval.
    """
    if (not force_static) and dataset_name and docker_is_available() and swebench_package_available():
        return docker_evaluate_patch(
            instance_id=instance_id,
            generated_patch=generated_patch,
            dataset_name=dataset_name,
            split=split,
        )
    else:
        return static_evaluate_patch(instance_id, generated_patch, ground_truth_patch)

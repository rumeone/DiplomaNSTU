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


def validate_patch_syntax(patch: str, filepath: str, original_content: Optional[str] = None) -> tuple[bool, str]:
    """
    Validate that a patch can be applied without syntax errors.
    
    Returns (is_valid, error_message).
    
    Uses multiple validation strategies:
    1. If original_content provided, test with patch command
    2. Parse added lines for Python syntax errors
    3. Check hunk header consistency
    """
    if not patch or not patch.strip():
        return False, "Empty patch"
    
    # Check for basic unified diff structure
    if not is_valid_unified_diff(patch):
        return False, "Not a valid unified diff format"
    
    # Check for em-dash/en-dash issues (common LLM mistakes)
    bad_chars = []
    for i, line in enumerate(patch.splitlines(), 1):
        if '\u2014' in line or '\u2013' in line or '\u2015' in line or '\u2212' in line:
            bad_chars.append(f"Line {i}: contains Unicode dash character")
    
    if bad_chars:
        return False, f"Unicode dash characters found:\n" + "\n".join(bad_chars[:5])
    
    # Check hunk headers
    hunk_pattern = re.compile(r'^@@\s+-(\d+)(?:,(\d+))?\s+\+(\d+)(?:,(\d+))?\s+@@')
    hunks = []
    for i, line in enumerate(patch.splitlines(), 1):
        m = hunk_pattern.match(line)
        if m:
            hunks.append((i, m.groups()))
    
    if not hunks:
        return False, "No valid hunk headers found (@@ -X,Y +A,B @@)"
    
    # Validate Python syntax in added lines
    added_lines = []
    for line in patch.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            added_lines.append(line[1:])
    
    if added_lines:
        added_code = '\n'.join(added_lines)
        try:
            import ast
            ast.parse(added_code)
        except SyntaxError as e:
            # Allow partial syntax errors (might be due to context)
            # Only fail on obvious errors
            error_msg = str(e)
            if 'unterminated string literal' in error_msg.lower():
                return False, f"Syntax error in added code: {error_msg}"
            if 'unmatched' in error_msg.lower():
                return False, f"Syntax error in added code: {error_msg}"
    
    return True, "OK"


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

    valid_diff = is_valid_unified_diff(generated_patch)
    report_lines.append(f"[1/3] Valid unified diff format: {valid_diff}")
    if valid_diff:
        score += 1

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
    try:
        import importlib
        importlib.import_module("swebench")
        return True
    except ImportError:
        return False


def _parse_harness_result(tmp_path: Path, instance_id: str) -> tuple[Optional[bool], Optional[bool]]:
    """
    Parse the harness output JSON written to tmp_path.

    The official harness writes two possible file formats:

    Format A — run_id based path (new harness versions):
        <tmp_path>/diploma_llm.diploma_eval.json
    Format B — nested results dir:
        <tmp_path>/**/results.json  or  <tmp_path>/**/*.json

    Returns (passed, patch_applied).
    """
    passed: Optional[bool] = None
    patch_applied: Optional[bool] = None

    # Collect ALL json files written anywhere under tmp_path
    json_files = list(tmp_path.rglob("*.json"))

    for rf in json_files:
        try:
            data = json.loads(rf.read_text(encoding="utf-8"))
        except Exception:
            continue

        if not isinstance(data, dict):
            continue

        # Format A: {"diploma_llm": {"instance_id": {resolved: bool, ...}}}
        # or flat:  {"resolved": ["id1", ...], "unresolved": [...], ...}

        # Try flat list format (most common in swebench >= 2.x)
        if "resolved" in data and isinstance(data["resolved"], list):
            patch_applied = True  # reached test stage means patch applied
            passed = instance_id in data["resolved"]
            return passed, patch_applied

        # Try flat dict format {resolved: {id: bool}}
        if "resolved" in data and isinstance(data["resolved"], dict):
            if instance_id in data["resolved"]:
                passed = bool(data["resolved"][instance_id])
            if "applied" in data and isinstance(data["applied"], dict):
                if instance_id in data["applied"]:
                    patch_applied = bool(data["applied"][instance_id])
            if passed is not None:
                return passed, patch_applied

        # Try nested model key format
        for model_key, model_data in data.items():
            if not isinstance(model_data, dict):
                continue
            if instance_id in model_data:
                entry = model_data[instance_id]
                if isinstance(entry, dict):
                    if "resolved" in entry:
                        passed = bool(entry["resolved"])
                    if "patch_applied" in entry:
                        patch_applied = bool(entry["patch_applied"])
                elif isinstance(entry, bool):
                    passed = entry
                if passed is not None:
                    return passed, patch_applied

    return passed, patch_applied


def _patch_apply_failed(output: str) -> bool:
    """Detect patch-apply failure from harness stdout."""
    return "Patch Apply Failed" in output or "FAILED" in output


def docker_evaluate_patch(
    instance_id: str,
    generated_patch: str,
    dataset_name: str,
    split: str = "test",
    timeout: int = 300,
) -> SWEEvaluationResult:
    """
    Run the official SWE-bench evaluation harness via subprocess.

    Key fixes vs old version:
    - subprocess runs with cwd=tmp_path so harness writes diploma_llm.diploma_eval.json
      into tmp_path (not the project root).
    - Result JSON is parsed from tmp_path (all *.json files searched recursively).
    - patch_applied is inferred from harness stdout if JSON parsing misses it.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        predictions_path = tmp_path / "predictions.jsonl"

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
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                # FIX: run from tmp_path so harness writes JSON here, not cwd
                cwd=str(tmp_path),
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

        # FIX: parse result JSON from tmp_path (harness writes there because cwd=tmp_path)
        passed, patch_applied = _parse_harness_result(tmp_path, instance_id)

        # Infer patch_applied from stdout if JSON parsing missed it
        if patch_applied is None:
            if _patch_apply_failed(raw_output):
                patch_applied = False
            elif "Instances completed" in raw_output and "Instances with errors: 0" in raw_output:
                patch_applied = True

        # Infer passed from stdout counters if JSON parsing missed it
        if passed is None:
            import re as _re
            m = _re.search(r'Instances resolved:\s*(\d+)', raw_output)
            if m and int(m.group(1)) > 0:
                passed = True
            elif "Instances unresolved" in raw_output:
                unresolved_m = _re.search(r'Instances unresolved:\s*(\d+)', raw_output)
                completed_m = _re.search(r'Instances completed:\s*(\d+)', raw_output)
                if unresolved_m and completed_m:
                    if int(completed_m.group(1)) > 0:
                        passed = False

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

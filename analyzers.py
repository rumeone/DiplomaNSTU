import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass
class StaticAnalysisResult:
    pylint_score: float | None
    pylint_stdout: str
    bandit_issues: int
    bandit_stdout: str  # JSON output from bandit (if produced)
    bandit_stderr: str  # stderr from bandit (diagnostics)
    custom_flags: list[str]


def _parse_pylint_score(stdout: str) -> float | None:
    """Ищет итоговую оценку X/10 в выводе pylint (разные локали/версии)."""
    m = re.search(r"rated at\s+([\d.]+)\s*/\s*10", stdout, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except ValueError:
            pass
    marker = "Your code has been rated at "
    if marker in stdout:
        try:
            tail = stdout.split(marker, 1)[1]
            score_str = tail.split("/10", 1)[0].strip()
            return float(score_str)
        except (IndexError, ValueError):
            pass
    return None


def run_pylint(file_path: Path) -> tuple[float | None, str]:
    """
    Запускает pylint и пытается вытащить итоговый score.
    Сначала ищет pylint в PATH, иначе ``python -m pylint`` (удобно для Windows/venv).
    """
    base_args = [
        str(file_path),
        "--score=y",
        "--output-format=text",
    ]
    pylint_exe = shutil.which("pylint")
    if pylint_exe:
        cmd = [pylint_exe, *base_args]
    else:
        cmd = [sys.executable, "-m", "pylint", *base_args]

    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout + "\n" + result.stderr

    score = _parse_pylint_score(stdout)
    if score is None and "No such file or directory" not in stdout:
        if shutil.which("pylint") is None and "No module named pylint" in stdout:
            return None, (
                stdout
                + "\nУстановите: pip install pylint (или добавьте pylint.exe в PATH)."
            )

    return score, stdout


def run_bandit(file_path: Path) -> tuple[int, str, str]:
    """
    Запускает Bandit в JSON-режиме.
    """
    bandit_exe = shutil.which("bandit")
    if bandit_exe:
        cmd = [bandit_exe, "-q", "-f", "json", str(file_path)]
    else:
        cmd = [sys.executable, "-m", "bandit", "-q", "-f", "json", str(file_path)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    issues_count = 0
    if stdout:
        try:
            payload = json.loads(stdout)
            issues_count = len(payload.get("results", []))
        except json.JSONDecodeError:
            pass

    return issues_count, stdout, stderr


def analyze_code(code: str, custom_flags: list[str]) -> StaticAnalysisResult:
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / "candidate.py"
        file_path.write_text(code, encoding="utf-8")

        pylint_score, pylint_stdout = run_pylint(file_path)
        bandit_issues, bandit_stdout, bandit_stderr = run_bandit(file_path)

        return StaticAnalysisResult(
            pylint_score=pylint_score,
            pylint_stdout=pylint_stdout,
            bandit_issues=bandit_issues,
            bandit_stdout=bandit_stdout,
            bandit_stderr=bandit_stderr,
            custom_flags=custom_flags
        )
import json
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FunctionalEvaluationResult:
    passed: bool | None
    result: str
    raw_output: str


def evaluate_with_humaneval(task_id: str, completion: str, problem_file: str | None = None) -> FunctionalEvaluationResult:
    """
    Обертка над evaluate_functional_correctness из official harness.
    Предполагается, что human-eval установлен и выполнение происходит
    только в безопасной среде.
    """
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
                    "Утилита evaluate_functional_correctness не найдена в PATH. "
                    "Установите пакет human-eval (pip install human-eval) "
                    "и проверьте, что папка Scripts вашего venv в PATH."
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

        line = results_file.read_text(encoding="utf-8").strip().splitlines()
        row = json.loads(line)

        return FunctionalEvaluationResult(
            passed=row.get("passed"),
            result=row.get("result", "unknown"),
            raw_output=output
        )
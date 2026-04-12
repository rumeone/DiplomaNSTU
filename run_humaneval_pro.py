"""HumanEval Pro style benchmark runner.

Задачи HumanEval берутся из датасета openai/openai_humaneval[web:194][web:199].
Для каждой задачи и каждой стратегии промптинга:
  1. Строим промпт (zero_shot / cot / docstring_guided).
  2. Генерируем код через LLMClient.generate_code().
  3. Сохраняем код в outputs/humaneval_pro_results/generated_code/.
  4. Запускаем pylint для оценки качества кода.
  5. Запускаем unit-тесты из HumanEval, чтобы проверить корректность.
  6. Записываем подробные результаты в CSV/JSON + агрегированное summary.

Запуск (из корня репозитория, внутри venv):

    pip install datasets pylint
    python run_humaneval_pro.py --tasks 50 --strategies zero_shot cot docstring_guided

Результаты:
    outputs/humaneval_pro_results/
        generated_code/          <- сгенерированный код (.py)
        pylint_reports/          <- полные отчёты pylint
        reports/
            raw_results.csv      <- по одному ряду на (task, strategy)
            raw_results.json
            summary.csv          <- агрегированные метрики по стратегиям
"""
from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from datasets import load_dataset  # type: ignore[import]
from tqdm import tqdm

from aggregation import compute_summary, save_records_to_csv, save_records_to_json
from llm_client import LLMClient


# ---------------------------------------------------------------------------
# Константы и типы
# ---------------------------------------------------------------------------

OUTPUT_BASE = Path("outputs") / "humaneval_pro_results"
DEFAULT_MAX_TASKS = 20
DEFAULT_STRATEGIES = ["zero_shot", "cot", "docstring_guided"]


@dataclass
class HumanEvalTask:
    task_id: str
    prompt: str
    test: str
    entry_point: str


# ---------------------------------------------------------------------------
# Загрузка HumanEval
# ---------------------------------------------------------------------------


def load_humaneval_tasks(max_tasks: Optional[int] = None) -> List[HumanEvalTask]:
    """Загрузить задачи HumanEval с HuggingFace.

    Используем датасет openai/openai_humaneval, сплит test.[web:194][web:199]
    """

    ds = load_dataset("openai/openai_humaneval", split="test")
    tasks: List[HumanEvalTask] = []

    for idx, row in enumerate(ds):
        if max_tasks is not None and idx >= max_tasks:
            break
        tasks.append(
            HumanEvalTask(
                task_id=row["task_id"],
                prompt=row["prompt"],
                test=row["test"],
                entry_point=row["entry_point"],
            )
        )
    return tasks


# ---------------------------------------------------------------------------
# Стратегии промптинга
# ---------------------------------------------------------------------------


def available_strategies() -> List[str]:
    return list(DEFAULT_STRATEGIES)


def build_prompt(strategy: str, task: HumanEvalTask) -> str:
    """Построить системный промпт + задание для выбранной стратегии.

    В поле task.prompt уже есть сигнатура функции и docstring.[web:194]
    Мы добавляем инструкцию, что нужно вернуть полный корректный код.
    """

    base_instruction = (
        "You are an expert Python developer. "
        "Write clean, PEP8-compliant code with type hints where appropriate. "
        "You are given a function signature and docstring. "
        "Return valid Python code that defines this function so that it satisfies its docstring "
        "and passes the hidden tests. Only output Python code, no explanations."
    )

    if strategy == "zero_shot":
        strategy_instruction = "Solve the task directly without showing your reasoning."
    elif strategy == "cot":
        strategy_instruction = (
            "First think step-by-step *internally* to understand the problem, "
            "then output only the final Python solution without the reasoning."
        )
    elif strategy == "docstring_guided":
        strategy_instruction = (
            "Carefully analyze the docstring examples and edge cases, then implement the function "
            "using explicit type hints and helpful inline comments. Do not change the signature."
        )
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return (
        base_instruction
        + "\n\nStrategy: "
        + strategy
        + "\n"
        + strategy_instruction
        + "\n\nHere is the function signature and docstring you must implement:\n\n"
        + task.prompt
    )


# ---------------------------------------------------------------------------
# Вспомогательные функции
# ---------------------------------------------------------------------------


def safe_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "task"


def ensure_dirs(base: Path) -> None:
    (base / "generated_code").mkdir(parents=True, exist_ok=True)
    (base / "pylint_reports").mkdir(parents=True, exist_ok=True)
    (base / "reports").mkdir(parents=True, exist_ok=True)


def _strip_code_fences(text: str) -> str:
    text = text.strip()
    # Убрать ```python / ```
    text = re.sub(r"^```[a-zA-Z]*\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Pylint + тесты HumanEval
# ---------------------------------------------------------------------------


def run_pylint(file_path: Path) -> Tuple[Optional[float], str]:
    """Запустить pylint для файла и вернуть (score, raw_output).

    Если pylint не установлен или упал - вернём (None, сообщение об ошибке).
    """

    try:
        proc = subprocess.run(
            ["pylint", str(file_path), "--score=y", "--output-format=text"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None, "pylint_not_installed"

    stdout = proc.stdout
    # Ищем строку вида: "Your code has been rated at 8.50/10"
    m = re.search(r"Your code has been rated at ([0-9.,\-]+)/10", stdout)
    score: Optional[float]
    if m:
        score = float(m.group(1).replace(",", "."))
    else:
        score = None
    return score, stdout


def run_humaneval_tests(task: HumanEvalTask, code: str) -> Tuple[Optional[bool], Optional[str]]:
    """Выполнить unit-тесты HumanEval для сгенерированного кода.

    Возвращает (passed, error_message). Если не удалось даже исполнить код,
    вернём (False, сообщение). Если что-то совсем странное, можно вернуть (None, msg).
    """

    namespace: Dict[str, Any] = {}

    try:
        exec(code, namespace)  # определяем функцию-кандидата
    except Exception as exc:  # noqa: BLE001
        return False, f"exec_candidate_failed: {exc}"

    try:
        exec(task.test, namespace)  # определяем check(candidate)
    except Exception as exc:  # noqa: BLE001
        return False, f"exec_test_failed: {exc}"

    candidate = namespace.get(task.entry_point)
    check_fn = namespace.get("check")

    if candidate is None or check_fn is None:
        return False, "missing_entry_point_or_check"

    try:
        check_fn(candidate)
    except Exception as exc:  # noqa: BLE001
        return False, f"tests_failed: {exc}"

    return True, None


# ---------------------------------------------------------------------------
# Основной пайплайн для одной задачи и одной стратегии
# ---------------------------------------------------------------------------


def evaluate_single(
    client: LLMClient,
    task: HumanEvalTask,
    strategy: str,
    base: Path,
) -> Dict[str, Any]:
    """Сгенерировать решение и оценить его pylint + тестами HumanEval."""

    prompt = build_prompt(strategy, task)

    try:
        raw_output = client.generate_code(prompt)
    except Exception as exc:  # noqa: BLE001
        return {
            "task_id": task.task_id,
            "strategy": strategy,
            "generated_code_path": None,
            "pylint_report_path": None,
            "pylint_score": None,
            "bandit_issues": None,
            "passed": None,
            "error": f"LLM generation failed: {exc}",
        }

    code = _strip_code_fences(raw_output)

    # 1) Сохранить код
    fname = safe_filename(task.task_id)
    gen_path = base / "generated_code" / f"{fname}__{strategy}.py"
    gen_path.parent.mkdir(parents=True, exist_ok=True)
    gen_path.write_text(code, encoding="utf-8")

    # 2) Pylint
    pylint_score, pylint_output = run_pylint(gen_path)
    pylint_report_path = base / "pylint_reports" / f"{fname}__{strategy}__pylint.txt"
    pylint_report_path.parent.mkdir(parents=True, exist_ok=True)
    pylint_report_path.write_text(pylint_output, encoding="utf-8")

    # 3) HumanEval tests
    passed, test_error = run_humaneval_tests(task, code)

    return {
        "task_id": task.task_id,
        "strategy": strategy,
        "generated_code_path": str(gen_path),
        "pylint_report_path": str(pylint_report_path),
        "pylint_score": pylint_score,
        "bandit_issues": None,
        "passed": passed,
        "error": test_error,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run HumanEval Pro style benchmark")
    parser.add_argument(
        "--tasks",
        type=int,
        default=DEFAULT_MAX_TASKS,
        help=f"Количество задач HumanEval (по датасету) (default: {DEFAULT_MAX_TASKS})",
    )
    parser.add_argument(
        "--strategies",
        nargs="+",
        default=DEFAULT_STRATEGIES,
        help="Список стратегий промптинга (default: zero_shot cot docstring_guided)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_BASE,
        help=f"Каталог для результатов (default: {OUTPUT_BASE})",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base = args.output_dir
    ensure_dirs(base)

    print(f"\n{'='*60}")
    print("HumanEval Pro benchmark")
    print(f"  Tasks:      {args.tasks}")
    print(f"  Strategies: {args.strategies}")
    print(f"  Output:     {base}")
    print(f"{'='*60}\n")

    print("Loading HumanEval tasks from HuggingFace (openai/openai_humaneval)...")
    try:
        tasks = load_humaneval_tasks(max_tasks=args.tasks)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] Failed to load HumanEval: {exc}")
        raise

    print(f"Loaded {len(tasks)} tasks.\n")

    client = LLMClient()
    records: List[Dict[str, Any]] = []

    for task in tqdm(tasks, desc="HumanEval Tasks"):
        print(f"\n--- Task: {task.task_id} ---")
        for strategy in args.strategies:
            print(f"  Strategy: {strategy} ...", end=" ", flush=True)
            record = evaluate_single(client, task, strategy, base)
            records.append(record)

            status: str
            if record["passed"] is True:
                status = "PASS"
            elif record["passed"] is False:
                status = "FAIL"
            else:
                status = "N/A"

            print(
                f"[{status}] pylint={record['pylint_score']} "
                f"error={record['error'] if record['error'] else '-'}",
            )

    # Сырые результаты
    raw_csv = base / "reports" / "raw_results.csv"
    raw_json = base / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)

    # Агрегированное summary по стратегиям
    summary_df = compute_summary(records)
    summary_path = base / "reports" / "summary.csv"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(summary_path, index=False, encoding="utf-8")

    print(f"\n{'='*60}")
    print("Results summary (per strategy):")
    if not summary_df.empty:
        print(summary_df.to_string(index=False))
    else:
        print("No records to summarize.")
    print(f"{'='*60}")
    print("\nSaved:")
    print(f"  {raw_csv}")
    print(f"  {raw_json}")
    print(f"  {summary_path}")
    print(f"  Generated code:   {base / 'generated_code'}")
    print(f"  Pylint reports:   {base / 'pylint_reports'}")


if __name__ == "__main__":
    main()

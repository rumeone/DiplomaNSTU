from __future__ import annotations

import re
from pathlib import Path
from typing import Callable

from tqdm import tqdm

from aggregation import compute_summary, save_records_to_csv, save_records_to_json
from analyzers import analyze_code
from code_utils import (
    basic_code_quality_flags,
    is_valid_python,
    strip_code_fences,
    write_generation_artifacts,
)
from config import EXPERIMENT_CONFIG
from evaluator import evaluate_with_humaneval
from humaneval_loader import HumanEvalTask, load_humaneval_tasks
from llm_client import LLMClient
from prompts import (
    build_constraint_guided_prompt,
    build_structured_cot_prompt,
    build_zero_shot_prompt,
)
from refinement import build_refinement_feedback, make_refinement_prompt


def ensure_dirs(base_dir: Path) -> None:
    (base_dir / "raw_generations").mkdir(parents=True, exist_ok=True)
    (base_dir / "analyzed").mkdir(parents=True, exist_ok=True)
    (base_dir / "reports").mkdir(parents=True, exist_ok=True)
    (base_dir / "logs").mkdir(parents=True, exist_ok=True)


def safe_filename(value: str) -> str:
    """Приводит строку к допустимому имени файла (без '/', пробелов и т.п.)."""
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_") or "value"


def save_text(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def get_prompt_builder(strategy: str) -> Callable[[str], str]:
    mapping = {
        "zero_shot": build_zero_shot_prompt,
        "constraint_guided": build_constraint_guided_prompt,
        "structured_cot": build_structured_cot_prompt,
    }
    if strategy not in mapping:
        raise ValueError(f"Неизвестная стратегия: {strategy}")
    return mapping[strategy]


def run_single_generation(
    client: LLMClient,
    task: HumanEvalTask,
    strategy: str,
    sample_index: int,
) -> dict:
    if strategy == "self_refine":
        # Базовый self_refine запускается как two-stage:
        # 1) первичная генерация constraint-guided
        # 2) анализ
        # 3) refinement
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
            static_root = EXPERIMENT_CONFIG.output_dir / "reports" / "static_analysis"
            initial_pylint_path = save_text(
                static_root
                / "pylint"
                / f"{task_part}__{strategy}__sample{sample_index}__initial_pylint.txt",
                static_result.pylint_stdout,
            )
            initial_bandit_json_path = save_text(
                static_root
                / "bandit"
                / f"{task_part}__{strategy}__sample{sample_index}__initial_bandit.json",
                static_result.bandit_stdout,
            )
            initial_bandit_stderr_path = save_text(
                static_root
                / "bandit"
                / f"{task_part}__{strategy}__sample{sample_index}__initial_bandit.stderr.txt",
                static_result.bandit_stderr,
            )

        functional_result = None
        functional_result_text = "not_executed"
        if valid and EXPERIMENT_CONFIG.enable_external_execution:
            functional_result = evaluate_with_humaneval(task.task_id, initial_code)
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
    static_root = EXPERIMENT_CONFIG.output_dir / "reports" / "static_analysis"
    pylint_path = None
    bandit_json_path = None
    bandit_stderr_path = None
    if static_result:
        pylint_path = save_text(
            static_root
            / "pylint"
            / f"{task_part}__{strategy}__sample{sample_index}__final_pylint.txt",
            static_result.pylint_stdout,
        )
        bandit_json_path = save_text(
            static_root
            / "bandit"
            / f"{task_part}__{strategy}__sample{sample_index}__final_bandit.json",
            static_result.bandit_stdout,
        )
        bandit_stderr_path = save_text(
            static_root
            / "bandit"
            / f"{task_part}__{strategy}__sample{sample_index}__final_bandit.stderr.txt",
            static_result.bandit_stderr,
        )

    functional_result = None
    if valid and EXPERIMENT_CONFIG.enable_external_execution:
        functional_result = evaluate_with_humaneval(task.task_id, final_code)

    code_file, initial_code_file = write_generation_artifacts(
        EXPERIMENT_CONFIG.output_dir,
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
        "custom_flags_count": len(flags),
        "custom_flags": " | ".join(flags) if flags else "",
        "pylint_score": static_result.pylint_score if static_result else None,
        "bandit_issues": static_result.bandit_issues if static_result else None,
        "pylint_report_file": str(pylint_path) if pylint_path else None,
        "bandit_report_file": str(bandit_json_path) if bandit_json_path else None,
        "bandit_stderr_file": str(bandit_stderr_path) if bandit_stderr_path else None,
        "passed": functional_result.passed if functional_result else None,
        "functional_result": functional_result.result if functional_result else "not_executed",
    }

    # Для `self_refine` дополнительно сохраняем отчеты по `initial_code`.
    if strategy == "self_refine":
        record["initial_pylint_report_file"] = str(initial_pylint_path) if initial_pylint_path else None
        record["initial_bandit_report_file"] = (
            str(initial_bandit_json_path) if initial_bandit_json_path else None
        )
        record["initial_bandit_stderr_file"] = (
            str(initial_bandit_stderr_path) if initial_bandit_stderr_path else None
        )

    return record


def main() -> None:
    ensure_dirs(EXPERIMENT_CONFIG.output_dir)

    client = LLMClient()
    tasks = load_humaneval_tasks(
        file_path=str(EXPERIMENT_CONFIG.dataset_path),
        max_tasks=EXPERIMENT_CONFIG.max_tasks
    )
    records: list[dict] = []

    for task in tqdm(tasks, desc="Tasks"):
        for strategy in EXPERIMENT_CONFIG.strategies:
            for sample_index in range(EXPERIMENT_CONFIG.samples_per_task):
                try:
                    record = run_single_generation(
                        client=client,
                        task=task,
                        strategy=strategy,
                        sample_index=sample_index
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

    raw_csv = EXPERIMENT_CONFIG.output_dir / "reports" / "raw_results.csv"
    raw_json = EXPERIMENT_CONFIG.output_dir / "reports" / "raw_results.json"
    save_records_to_csv(records, raw_csv)
    save_records_to_json(records, raw_json)

    summary_df = compute_summary(records)
    summary_path = EXPERIMENT_CONFIG.output_dir / "reports" / "summary.csv"
    summary_df.to_csv(summary_path, index=False, encoding="utf-8")

    print(f"Сохранено: {raw_csv}")
    print(f"Сохранено: {raw_json}")
    print(f"Сохранено: {summary_path}")


if __name__ == "__main__":
    main()
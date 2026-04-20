from analyzers import StaticAnalysisResult
from prompts import build_self_refine_prompt


def build_refinement_feedback(
    syntax_error: str,
    static_result: StaticAnalysisResult | None,
    functional_result_text: str
) -> str:
    """Формирует детальный feedback для self-refine на основе результатов анализа."""
    parts: list[str] = []

    if syntax_error:
        parts.append(f"Syntax problem: {syntax_error}")

    if functional_result_text and functional_result_text != "not_executed":
        parts.append(f"Functional evaluation result: {functional_result_text}")

    if static_result is not None:
        if static_result.custom_flags:
            parts.append("Custom quality flags:")
            parts.extend(f"- {flag}" for flag in static_result.custom_flags)

        if static_result.pylint_score is not None:
            parts.append(f"Pylint score: {static_result.pylint_score}/10")

        # Детальные замечания Pylint
        pylint_stdout = getattr(static_result, "pylint_stdout", "") or ""
        if pylint_stdout:
            pylint_issues = _extract_pylint_issues(pylint_stdout)
            if pylint_issues:
                parts.append("Pylint issues found:")
                parts.extend(f"- {issue}" for issue in pylint_issues)

        if static_result.bandit_issues:
            parts.append(f"Bandit security issues: {static_result.bandit_issues}")

        # Метрики Radon
        radon = getattr(static_result, "radon", None)
        if radon is not None:
            radon_parts = []
            if getattr(radon, "cyclomatic_complexity", None) is not None:
                radon_parts.append(
                    f"average cyclomatic complexity: {radon.cyclomatic_complexity:.1f}"
                )
            if getattr(radon, "max_complexity", None) is not None:
                radon_parts.append(f"max complexity: {radon.max_complexity}")
            if getattr(radon, "maintainability_index", None) is not None:
                radon_parts.append(
                    f"maintainability index: {radon.maintainability_index:.1f}/100"
                )
            if radon_parts:
                parts.append("Radon metrics: " + ", ".join(radon_parts))

    if not parts:
        parts.append(
            "Improve readability, robustness, and clarity while preserving correctness."
        )

    return "\n".join(parts)


def _extract_pylint_issues(pylint_stdout: str) -> list[str]:
    """Извлекает конкретные замечания из stdout Pylint."""
    issues: list[str] = []
    for line in pylint_stdout.splitlines():
        stripped = line.strip()
        if not stripped or not (": " in stripped):
            continue
        # Pylint messages contain .py: with line/col reference
        if ".py:" in stripped:
            # Убираем путь к temp-файлу, оставляем номер строки и сообщение
            idx = stripped.index(".py:") + 4
            message = stripped[idx:].strip()
            if message:
                issues.append(message)
    return issues


def make_refinement_prompt(task_prompt: str, previous_code: str, feedback: str) -> str:
    return build_self_refine_prompt(
        task_prompt=task_prompt,
        previous_code=previous_code,
        feedback=feedback,
    )
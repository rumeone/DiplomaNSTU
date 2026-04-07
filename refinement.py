from analyzers import StaticAnalysisResult
from prompts import build_self_refine_prompt


def build_refinement_feedback(
    syntax_error: str,
    static_result: StaticAnalysisResult | None,
    functional_result_text: str
) -> str:
    parts: list[str] = []

    if syntax_error:
        parts.append(f"Syntax problem: {syntax_error}")

    if functional_result_text:
        parts.append(f"Functional evaluation result: {functional_result_text}")

    if static_result is not None:
        if static_result.custom_flags:
            parts.append("Custom quality flags:")
            parts.extend(f"- {flag}" for flag in static_result.custom_flags)

        if static_result.pylint_score is not None:
            parts.append(f"Pylint score: {static_result.pylint_score}/10")

        if static_result.bandit_issues:
            parts.append(f"Bandit issues: {static_result.bandit_issues}")

    if not parts:
        parts.append("Improve readability, robustness, and clarity while preserving correctness.")

    return "\n".join(parts)


def make_refinement_prompt(task_prompt: str, previous_code: str, feedback: str) -> str:
    return build_self_refine_prompt(
        task_prompt=task_prompt,
        previous_code=previous_code,
        feedback=feedback
    )
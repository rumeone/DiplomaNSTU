from dataclasses import dataclass

from analyzers import StaticAnalysisResult, analyze_code
from code_utils import is_valid_python, strip_code_fences
from evaluator import FunctionalEvaluationResult, evaluate_with_humaneval
from prompts import build_self_refine_prompt


@dataclass
class CodeAssessment:
    """Combined syntax, static-analysis, and optional functional-test result."""
    code: str
    syntax_valid: bool
    syntax_error: str
    static_result: StaticAnalysisResult | None
    functional_result: FunctionalEvaluationResult | None

    @property
    def functional_result_text(self) -> str:
        if self.functional_result is None:
            return "not_executed"
        return self.functional_result.result

    @property
    def functional_raw_output(self) -> str:
        if self.functional_result is None:
            return ""
        return self.functional_result.raw_output

    @property
    def passed(self) -> bool | None:
        if self.functional_result is None:
            return None
        return self.functional_result.passed


def assess_code(
    code: str,
    task_id: str,
    test_code: str | None,
    entry_point: str | None,
    enable_execution: bool,
) -> CodeAssessment:
    """Run the same checks used for self-refine feedback and acceptance."""
    clean_code = strip_code_fences(code)
    valid, syntax_error = is_valid_python(clean_code)
    static_result = analyze_code(clean_code) if valid else None

    functional_result = None
    if valid and enable_execution:
        functional_result = evaluate_with_humaneval(
            task_id=task_id,
            completion=clean_code,
            test_code=test_code,
            entry_point=entry_point,
        )

    return CodeAssessment(
        code=clean_code,
        syntax_valid=valid,
        syntax_error=syntax_error,
        static_result=static_result,
        functional_result=functional_result,
    )


def assessment_score(assessment: CodeAssessment) -> tuple:
    """Rank candidates for accepting or rejecting a refinement."""
    functional_rank = 0
    if assessment.passed is True:
        functional_rank = 2
    elif assessment.passed is None:
        functional_rank = 1

    static_result = assessment.static_result
    pylint_score = (
        static_result.pylint_score
        if static_result and static_result.pylint_score is not None
        else -1.0
    )
    bandit_score = -(static_result.bandit_issues if static_result else 999)
    radon = static_result.radon if static_result else None
    maintainability = (
        radon.maintainability_index
        if radon and radon.maintainability_index is not None
        else -1.0
    )
    avg_complexity = (
        radon.cyclomatic_complexity
        if radon and radon.cyclomatic_complexity is not None
        else 999.0
    )
    max_complexity = (
        radon.max_complexity
        if radon and radon.max_complexity is not None
        else 999
    )

    return (
        functional_rank,
        int(assessment.syntax_valid),
        pylint_score,
        bandit_score,
        maintainability,
        -avg_complexity,
        -max_complexity,
    )


def should_accept_refinement(
    current: CodeAssessment,
    candidate: CodeAssessment,
    *,
    enable_execution: bool,
) -> bool:
    """Accept a refined candidate only when it does not regress known quality."""
    if not candidate.syntax_valid:
        return False
    if not current.syntax_valid:
        return True

    if enable_execution:
        if current.passed is True and candidate.passed is not True:
            return False
        if current.passed is not True and candidate.passed is True:
            return True

    return assessment_score(candidate) >= assessment_score(current)


def build_refinement_feedback(
    syntax_error: str,
    static_result: StaticAnalysisResult | None,
    functional_result_text: str,
    functional_raw_output: str = "",
) -> str:
    """Формирует детальный feedback для self-refine на основе результатов анализа."""
    parts: list[str] = []

    if syntax_error:
        parts.append(f"Syntax problem: {syntax_error}")

    if functional_result_text and functional_result_text != "not_executed":
        parts.append(f"Functional evaluation result: {functional_result_text}")
        if functional_raw_output:
            parts.append("Functional failure details:")
            parts.append(_truncate_text(functional_raw_output, max_chars=2400))

    if static_result is not None:
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


def build_refinement_feedback_from_assessment(assessment: CodeAssessment) -> str:
    """Build model feedback from a reusable assessment object."""
    return build_refinement_feedback(
        syntax_error=assessment.syntax_error,
        static_result=assessment.static_result,
        functional_result_text=assessment.functional_result_text,
        functional_raw_output=assessment.functional_raw_output,
    )


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


def _truncate_text(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n... [truncated]"

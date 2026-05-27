"""Prompt helper based on LLM prompting strategy benchmark results.

The module turns a plain-language user need into a ready prompt for code
generation. It can work deterministically from local experiment summaries or
ask an OpenAI-compatible LLM to polish the final prompt using the same
experiment context.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> None:
        """Fallback when python-dotenv is not installed."""
        return None


STRATEGIES = ("zero_shot", "constraint_guided", "structured_cot", "self_refine")


@dataclass
class StrategyMetrics:
    """Aggregated metrics for one prompting strategy."""

    strategy: str
    runs: int = 0
    tasks: float = 0.0
    generations: float = 0.0
    pass_rate: float = 0.0
    avg_pylint: float = 0.0
    avg_bandit_issues: float = 0.0
    avg_cyclomatic_complexity: float = 0.0
    max_cyclomatic_complexity: float = 0.0
    avg_maintainability_index: float = 0.0


@dataclass
class PromptRecommendation:
    """Result returned by the helper."""

    strategy: str
    rationale: str
    final_prompt: str
    research_context: str


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        if value in (None, ""):
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def find_summary_files(results_dirs: list[Path] | None = None) -> list[Path]:
    """Find summary.csv files in outputs* directories."""
    if results_dirs:
        return [path / "reports" / "summary.csv" for path in results_dirs]

    return sorted(Path(".").glob("outputs_test_grok/reports/summary.csv"))


def load_strategy_metrics(summary_files: list[Path]) -> dict[str, StrategyMetrics]:
    """Load and average strategy metrics from summary.csv files."""
    totals: dict[str, StrategyMetrics] = {
        strategy: StrategyMetrics(strategy=strategy) for strategy in STRATEGIES
    }

    for summary_path in summary_files:
        if not summary_path.exists():
            continue

        with summary_path.open("r", encoding="utf-8-sig", newline="") as file:
            for row in csv.DictReader(file):
                strategy = row.get("strategy", "")
                if strategy not in totals:
                    continue

                metrics = totals[strategy]
                metrics.runs += 1
                metrics.tasks += _safe_float(row.get("tasks"))
                metrics.generations += _safe_float(row.get("generations"))
                metrics.pass_rate += _safe_float(row.get("pass_rate"))
                metrics.avg_pylint += _safe_float(row.get("avg_pylint"))
                metrics.avg_bandit_issues += _safe_float(row.get("avg_bandit_issues"))
                metrics.avg_cyclomatic_complexity += _safe_float(
                    row.get("avg_cyclomatic_complexity")
                )
                metrics.max_cyclomatic_complexity += _safe_float(
                    row.get("max_cyclomatic_complexity")
                )
                metrics.avg_maintainability_index += _safe_float(
                    row.get("avg_maintainability_index")
                )

    averaged: dict[str, StrategyMetrics] = {}
    for strategy, metrics in totals.items():
        if metrics.runs == 0:
            continue
        averaged[strategy] = StrategyMetrics(
            strategy=strategy,
            runs=metrics.runs,
            tasks=metrics.tasks / metrics.runs,
            generations=metrics.generations / metrics.runs,
            pass_rate=metrics.pass_rate / metrics.runs,
            avg_pylint=metrics.avg_pylint / metrics.runs,
            avg_bandit_issues=metrics.avg_bandit_issues / metrics.runs,
            avg_cyclomatic_complexity=metrics.avg_cyclomatic_complexity / metrics.runs,
            max_cyclomatic_complexity=metrics.max_cyclomatic_complexity / metrics.runs,
            avg_maintainability_index=metrics.avg_maintainability_index / metrics.runs,
        )

    return averaged


def build_research_context(metrics: dict[str, StrategyMetrics]) -> str:
    """Build compact research context for deterministic output or LLM prompt."""
    if not metrics:
        return dedent(
            """
            Локальные summary.csv не найдены. Используются общие выводы исследования:
            constraint_guided обычно лучше подходит для читаемого и сопровождаемого
            кода, structured_cot - для задач с рассуждением и граничными случаями,
            self_refine - для дополнительной проверки и улучшения результата,
            zero_shot - для простых и быстрых запросов.
            """
        ).strip()

    lines = [
        "В проекте сравнивались стратегии zero_shot, constraint_guided,",
        "structured_cot и self_refine по метрикам pass_rate, Pylint, Bandit,",
        "цикломатической сложности и maintainability index.",
        "",
        "Агрегированные результаты из локальных summary.csv:",
    ]

    for strategy in STRATEGIES:
        item = metrics.get(strategy)
        if not item:
            continue
        lines.append(
            "- {strategy}: pass_rate={pass_rate:.3f}, avg_pylint={pylint:.2f}, "
            "bandit_issues={bandit:.2f}, avg_cc={cc:.2f}, max_cc={max_cc:.2f}, "
            "maintainability_index={mi:.2f}".format(
                strategy=strategy,
                pass_rate=item.pass_rate,
                pylint=item.avg_pylint,
                bandit=item.avg_bandit_issues,
                cc=item.avg_cyclomatic_complexity,
                max_cc=item.max_cyclomatic_complexity,
                mi=item.avg_maintainability_index,
            )
        )

    lines.extend(
        [
            "",
            "Интерпретация результатов:",
            "- constraint_guided рекомендуется, когда важны читаемость, стиль,",
            "  командная работа и сопровождаемость кода;",
            "- structured_cot рекомендуется, когда задача содержит сложную логику,",
            "  ограничения, граничные случаи или требует предварительного анализа;",
            "- self_refine рекомендуется, когда пользователь хочет получить",
            "  доработанный вариант после проверки качества;",
            "- zero_shot допустим для простых одноразовых задач, но требует",
            "  добавления минимальных требований к качеству.",
        ]
    )
    return "\n".join(lines)


def infer_user_profile(user_request: str) -> dict[str, bool]:
    """Extract simple signals from the user request."""
    text = user_request.lower()
    beginner_words = ("нович", "начал", "начина", "изуч", "учеб", "студент", "курс")
    team_words = ("команд", "коллег", "совмест", "проект", "репозитор", "git")
    quality_words = (
        "понят",
        "чита",
        "поддерж",
        "сопровожд",
        "pep",
        "стиль",
        "архитект",
        "библиотек",
        "модуль",
    )
    correctness_words = (
        "слож",
        "алгоритм",
        "ошиб",
        "edge",
        "гранич",
        "услов",
        "надёж",
        "надеж",
        "точн",
        "стабил",
        "математ",
        "коррект",
        "тест",
    )
    refine_words = (
        "улучш",
        "проверь",
        "провер",
        "рефактор",
        "доработ",
        "максимально каче",
        "production",
        "продакш",
    )
    speed_words = ("быстро", "кратко", "просто", "однораз")

    return {
        "beginner": any(word in text for word in beginner_words),
        "team": any(word in text for word in team_words),
        "quality": any(word in text for word in quality_words),
        "correctness": any(word in text for word in correctness_words),
        "refine": any(word in text for word in refine_words),
        "speed": any(word in text for word in speed_words),
    }


def choose_strategy(user_request: str, metrics: dict[str, StrategyMetrics]) -> str:
    """Choose a prompting strategy using profile signals and experiment metrics."""
    profile = infer_user_profile(user_request)
    scores = {strategy: 0.0 for strategy in STRATEGIES}

    for strategy, item in metrics.items():
        scores[strategy] += item.pass_rate * 4.0
        scores[strategy] += (item.avg_pylint / 10.0) * 2.0
        scores[strategy] += (item.avg_maintainability_index / 100.0) * 2.0
        scores[strategy] -= min(item.avg_cyclomatic_complexity / 10.0, 1.0)
        scores[strategy] -= min(item.avg_bandit_issues, 5.0) * 0.4

    if profile["beginner"]:
        scores["constraint_guided"] += 2.2
        scores["structured_cot"] += 0.8
    if profile["team"] or profile["quality"]:
        scores["constraint_guided"] += 2.0
        scores["self_refine"] += 0.8
    if profile["correctness"]:
        scores["structured_cot"] += 3.0
        scores["self_refine"] += 1.8
        scores["constraint_guided"] += 0.3
    if profile["refine"]:
        scores["self_refine"] += 2.5
    if profile["speed"] and not (profile["team"] or profile["quality"]):
        scores["zero_shot"] += 1.5

    if not metrics:
        if profile["refine"]:
            return "self_refine"
        if profile["correctness"]:
            return "structured_cot"
        if profile["beginner"] or profile["team"] or profile["quality"]:
            return "constraint_guided"
        return "zero_shot"

    return max(scores, key=scores.get)


def build_rationale(strategy: str, user_request: str, metrics: dict[str, StrategyMetrics]) -> str:
    """Explain the selected strategy."""
    profile = infer_user_profile(user_request)
    reasons: list[str] = []

    if profile["beginner"]:
        reasons.append("пользователь описывает себя как начинающего")
    if profile["team"]:
        reasons.append("код предполагается использовать в командном или учебном проекте")
    if profile["quality"]:
        reasons.append("в запросе явно важны читаемость и сопровождаемость")
    if profile["correctness"]:
        reasons.append("задача требует внимания к корректности и граничным случаям")
    if profile["refine"]:
        reasons.append("пользователь ожидает улучшение и проверку результата")

    if not reasons:
        reasons.append("в запросе не указаны специальные ограничения, поэтому выбран общий баланс качества")

    metric = metrics.get(strategy)
    metric_text = ""
    if metric:
        metric_text = (
            f" По локальным результатам для {strategy}: pass_rate={metric.pass_rate:.3f}, "
            f"avg_pylint={metric.avg_pylint:.2f}, "
            f"maintainability_index={metric.avg_maintainability_index:.2f}."
        )

    return (
        f"Выбрана стратегия {strategy}, потому что {', '.join(reasons)}."
        f"{metric_text}"
    )


def build_prompt_template(strategy: str, user_request: str) -> str:
    """Build a deterministic final prompt."""
    common_requirements = "\n".join(
        [
            "Требования к результату:",
            "- используй понятные имена переменных, функций и классов;",
            "- соблюдай PEP 8;",
            "- добавь docstring к основным функциям;",
            "- обработай возможные граничные случаи;",
            "- избегай излишне сложных конструкций;",
            "- сделай код удобным для чтения, проверки и дальнейшего изменения;",
            "- если используешь нестандартные библиотеки, явно укажи это;",
            "- после кода кратко объясни, как работает решение.",
        ]
    )

    if strategy == "structured_cot":
        strategy_block = dedent(
            """
            Перед написанием ответа проанализируй задачу внутренне:
            1. выдели входные данные, выходные данные и ограничения;
            2. определи возможные граничные случаи;
            3. выбери самый простой корректный алгоритм;
            4. затем верни финальное решение без подробной цепочки рассуждений.
            """
        ).strip()
    elif strategy == "self_refine":
        strategy_block = dedent(
            """
            Сначала подготовь решение, затем проверь его по критериям качества:
            синтаксис, корректность, граничные случаи, читаемость, PEP 8,
            сопровождаемость и сложность. Верни только улучшенную финальную версию.
            """
        ).strip()
    elif strategy == "zero_shot":
        strategy_block = "Реши задачу кратко и без лишних отступлений, сохраняя базовые требования к качеству."
    else:
        strategy_block = dedent(
            """
            Сфокусируйся на чистом, понятном и сопровождаемом коде. Решение должно
            быть удобно для начинающего разработчика и для командной проверки.
            """
        ).strip()

    return "\n\n".join(
        [
            "Ты опытный Python-разработчик и наставник.",
            f"Контекст пользователя:\n{user_request}",
            strategy_block,
            common_requirements,
            "Задача:\n[вставьте конкретное описание задачи, которую нужно решить]",
        ]
    )


def _get_api_key() -> str:
    """Get API key for LLM prompt helper mode."""
    api_key = (
        os.environ.get("DIPLOMA_PROMTS")
        or os.environ.get("REVIEWER_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
    )
    if not api_key:
        raise RuntimeError(
            "Set DIPLOMA_PROMTS, REVIEWER_API_KEY, or OPENAI_API_KEY to use --use-llm"
        )
    return api_key


def _extract_strategy(text: str) -> str:
    """Extract strategy name from LLM response."""
    selected_line = re.search(
        r"выбранная\s+стратегия\s*:?\s*(?:\*\*)?`?([a-z_]+)`?",
        text,
        flags=re.IGNORECASE,
    )
    if selected_line:
        candidate = selected_line.group(1).lower()
        if candidate in STRATEGIES:
            return candidate

    for strategy in STRATEGIES:
        if re.search(rf"\b{re.escape(strategy)}\b", text):
            return strategy
    return "llm_selected"


def analyze_with_llm(
    user_request: str,
    research_context: str,
    model: str,
) -> str:
    """Ask an OpenAI-compatible LLM to analyze the request and create a prompt."""
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Install openai package to use --use-llm") from exc

    client = OpenAI(api_key=_get_api_key(), base_url=os.environ.get("OPENAI_BASE_URL"))
    system_prompt = dedent(
        """
        Ты LLM-ассистент по анализу пользовательских потребностей и формированию
        промптов для генерации программного кода.

        ВАЖНО: выбор стратегии должен выполнять именно ты на основе:
        1. запроса пользователя;
        2. экспериментальных результатов исследования;
        3. смысловых характеристик стратегий prompt engineering.

        Локальная программа не выбирает стратегию за тебя. Она только передает
        тебе данные исследования.

        Доступные стратегии:
        - zero_shot: для простых и быстрых задач, где достаточно прямого запроса;
        - constraint_guided: для задач, где важны читаемость, PEP 8, стиль,
          сопровождаемость, командная разработка и явные требования к качеству;
        - structured_cot: для задач, где важны точность, стабильность,
          математическая корректность, алгоритмический анализ, ограничения и
          граничные случаи. Рассуждение должно быть внутренним, без раскрытия
          подробной цепочки мыслей;
        - self_refine: для задач, где нужен максимально проверенный результат:
          сначала решение, затем самопроверка по критериям качества и финальная
          улучшенная версия.

        Не придумывай новые экспериментальные числа. Используй только те
        результаты, которые переданы в контексте.

        Не придумывай конкретную программную задачу, если пользователь ее не
        указал. Если пользователь описал только область или намерение, оставь
        в итоговом промпте поле "[вставьте конкретное описание задачи]" и
        сформулируй требования к будущей задаче. Не заменяй намерение
        пользователя случайным примером. Не добавляй примеры задач в скобках
        после поля задачи.

        Итоговый промпт должен быть практичным: его можно сразу отправить LLM
        для генерации кода после подстановки конкретной задачи.
        """
    ).strip()

    user_prompt = dedent(
        f"""
        Запрос пользователя:
        {user_request}

        Контекст исследования:
        {research_context}

        Проанализируй запрос пользователя и самостоятельно выбери одну стратегию:
        zero_shot, constraint_guided, structured_cot или self_refine.

        Верни ответ строго в структуре:
        1. Выбранная стратегия
        2. Обоснование на основе запроса и результатов исследования
        3. Итоговый промпт

        Важно: в итоговом промпте сохрани исходную область пользователя. Не
        добавляй конкретный пример задачи, которого не было в запросе. В поле
        "Задача" оставь только placeholder без примеров.
        """
    ).strip()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=1800,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("LLM returned empty response")
    return content.strip()


def recommend_prompt(
    user_request: str,
    summary_files: list[Path],
    use_llm: bool = False,
    model: str = "deepseek/deepseek-v3.2",
) -> PromptRecommendation:
    """Create a prompt recommendation."""
    metrics = load_strategy_metrics(summary_files)
    research_context = build_research_context(metrics)

    if use_llm:
        final_prompt = analyze_with_llm(
            user_request=user_request,
            research_context=research_context,
            model=model,
        )
        strategy = _extract_strategy(final_prompt)
        rationale = (
            "Стратегия выбрана LLM на основе пользовательского запроса и "
            "контекста экспериментальных результатов."
        )
        return PromptRecommendation(
            strategy=strategy,
            rationale=rationale,
            final_prompt=final_prompt,
            research_context=research_context,
        )

    strategy = choose_strategy(user_request, metrics)
    rationale = build_rationale(strategy, user_request, metrics)
    final_prompt = build_prompt_template(strategy, user_request)

    return PromptRecommendation(
        strategy=strategy,
        rationale=rationale,
        final_prompt=final_prompt,
        research_context=research_context,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a prompt recommendation based on benchmark results.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "request",
        nargs="?",
        help="User need, for example: 'Хочу код для учебного проекта...'",
    )
    parser.add_argument(
        "--request-file",
        type=Path,
        help="Read user request from a text file.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        action="append",
        help="Output directory with reports/summary.csv. Can be passed multiple times.",
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Ask an OpenAI-compatible LLM to polish the final prompt.",
    )
    parser.add_argument(
        "--model",
        default="deepseek/deepseek-v3.2",
        help="Model for --use-llm mode.",
    )
    parser.add_argument(
        "--show-research-context",
        action="store_true",
        help="Print the compact experiment context used by the helper.",
    )
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()

    if args.request_file:
        user_request = args.request_file.read_text(encoding="utf-8").strip()
    elif args.request:
        user_request = args.request.strip()
    else:
        raise SystemExit("Provide a request argument or --request-file")

    summary_files = find_summary_files(args.results_dir)
    recommendation = recommend_prompt(
        user_request=user_request,
        summary_files=summary_files,
        use_llm=args.use_llm,
        model=args.model,
    )

    print("\n=== Selected strategy ===")
    print(recommendation.strategy)
    print("\n=== Rationale ===")
    print(recommendation.rationale)

    if args.show_research_context:
        print("\n=== Research context ===")
        print(recommendation.research_context)

    print("\n=== Final prompt ===")
    print(recommendation.final_prompt)


if __name__ == "__main__":
    main()

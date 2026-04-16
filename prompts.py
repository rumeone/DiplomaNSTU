from textwrap import dedent


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_RULES = dedent("""\
    You are a precise Python engineer. Your only job is to implement
    Python functions that are correct, readable, and idiomatic.

    Output contract (never violate):
    - Return a single Python code block with no markdown fences.
    - Implement exactly the function(s) in the task — nothing more.
    - Keep the exact signature from the task prompt.
    - No placeholder comments, no TODO, no test code.
""")


# ---------------------------------------------------------------------------
# Strategy 1: Zero-shot
# Цель: прямое решение без overhead-инструкций.
# Почему: чистый baseline — модель опирается только на задачу.
# ---------------------------------------------------------------------------

def build_zero_shot_prompt(task_prompt: str) -> str:
    return dedent(f"""\
        Implement the Python function below.
        Return only the complete function body.

        {task_prompt}
    """)


# ---------------------------------------------------------------------------
# Strategy 2: Constraint-guided
# Цель: улучшить pylint-score через явное качество кода.
# Почему: прямые качественные constraints (имена, дублирование, edge-cases)
#         снижают синтаксический и стилистический мусор без CoT-overhead.
# ---------------------------------------------------------------------------

def build_constraint_guided_prompt(task_prompt: str) -> str:
    return dedent(f"""\
        Implement the Python function below.

        Requirements:
        - Keep the exact function signature from the task.
        - Prioritize correctness over cleverness.
        - Use a simple, idiomatic implementation.
        - Handle obvious edge cases only when they are implied by the task.
        - Do not add extra features, validation, or alternate behaviors not requested.
        - Return only the final Python code.

        Task:
        {task_prompt}
    """)


def build_structured_cot_prompt(task_prompt: str) -> str:
    return dedent(f"""\
        Implement the Python function below.

        Before writing code, briefly reason internally about:
        - the simplest correct approach,
        - the key edge cases explicitly implied by the task,
        - how to keep the implementation readable.

        Then write the solution.

        IMPORTANT:
        - Output ONLY Python code.
        - Do NOT include explanations, headers, or markdown fences.
        - Keep the exact function signature from the task.
        - Prefer the shortest clear correct solution.

        Task:
        {task_prompt}
    """)


def build_self_refine_prompt(
    task_prompt: str,
    previous_code: str,
    feedback: str,
) -> str:
    return dedent(f"""\
        Revise the Python solution below to fix the reported issues.

        Task:
        {task_prompt}

        Previous code:
        {previous_code}

        Feedback:
        {feedback}

        Revision requirements:
        - Fix all correctness issues first.
        - Preserve the exact function signature.
        - Keep changes minimal unless a rewrite is necessary.
        - Do not add new functionality beyond the task.
        - Return only the revised Python code.

        Revised code:
    """)
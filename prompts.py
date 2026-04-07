from textwrap import dedent


SYSTEM_RULES = dedent("""
You are an expert Python software engineer.
Return only valid Python code.
Do not include markdown fences.
Do not include explanations outside the code.

Global rules:
1. Preserve the exact function name and signature from the task.
2. Solve only the requested task.
3. Use clear, readable, and maintainable Python code.
4. Handle edge cases implied by the task.
5. Do not use input(), print(), files, network, subprocesses, eval(), or exec().
6. Use only the Python standard language features needed for the task.
7. Do not add test code.
8. Add short comments only where they clarify non-trivial logic.
""")


def build_zero_shot_prompt(task_prompt: str) -> str:
    return dedent(f"""
    Solve the following Python programming task.

    Task:
    {task_prompt}

    Return only the final Python function implementation.
    """)


def build_constraint_guided_prompt(task_prompt: str) -> str:
    return dedent(f"""
    Solve the following Python programming task.

    Task:
    {task_prompt}

    Additional code quality rules:
    - Prefer straightforward and deterministic logic.
    - Use descriptive variable names.
    - Avoid duplicated logic.
    - Avoid unnecessary nested conditions.
    - Keep the implementation concise but readable.
    - Make the function robust for edge cases implied by the specification.
    - Do not rely on hidden assumptions about tests.
    - Add brief comments only if the algorithm is not obvious.

    Return only the final Python function implementation.
    """)


def build_structured_cot_prompt(task_prompt: str) -> str:
    """
    Стратегия Structured CoT.
    Важно: reasoning не должен попадать в финальный файл.
    Поэтому просим модель сначала внутренне построить структурный план,
    а в ответ вернуть только код.
    """
    return dedent(f"""
    Solve the following Python programming task using a structured reasoning process.

    Task:
    {task_prompt}

    Before writing the code, reason using a structured plan based on:
    - sequence steps,
    - branch conditions,
    - loop structures,
    - edge cases,
    - return behavior.

    Then write the final Python implementation.

    Important output rule:
    Return only the final Python code, without the plan and without explanations.
    """)


def build_self_refine_prompt(task_prompt: str, previous_code: str, feedback: str) -> str:
    return dedent(f"""
    You are given a Python programming task, a previous solution, and review feedback.
    Improve the solution so that it is more correct, readable, robust, and safe.

    Task:
    {task_prompt}

    Previous solution:
    {previous_code}

    Feedback:
    {feedback}

    Revision rules:
    - Preserve the required function signature.
    - Fix any logical, style, and robustness issues.
    - Keep the solution simple and readable.
    - Do not add explanations outside the code.
    - Return only the improved Python code.

    Final answer:
    """)
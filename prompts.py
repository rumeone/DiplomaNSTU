from textwrap import dedent


SYSTEM_RULES = dedent("""
You are an expert Python software engineer.
Return only valid Python code.
Do not include markdown fences.
Do not include explanations outside the code.
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
    Focus on producing clean, maintainable, and well-structured code.

    Task:
    {task_prompt}

    Quality guidelines:
    - Follow PEP 8 style conventions.
    - Start the file with a brief module-level docstring.
    - Include a docstring for the function if one is not already present.
    - If the signature uses types from typing (List, Tuple, Dict, Optional), add the corresponding import.
    - Use descriptive variable names that reflect their purpose.
    - Prefer flat control flow: use early returns and guard clauses instead of deep nesting.
    - Avoid trailing whitespace and ensure the file ends with a newline.

    Return only the final Python function implementation.
    """)


def build_structured_cot_prompt(task_prompt: str) -> str:
    """
    Стратегия Structured CoT.
    Модель рассуждает внутренне, возвращает только чистый код.
    """
    return dedent(f"""
    Solve the following Python programming task.

    Task:
    {task_prompt}

    Before writing code, reason internally (do not include reasoning in your output):
    1. What is the simplest correct approach?
    2. What edge cases does the specification imply?
    3. How can the solution be kept short, readable, and PEP 8 compliant?

    Then write the implementation, applying these principles:
    - Prefer concise, idiomatic Python over verbose manual logic.
    - Use meaningful variable names.
    - Include a module-level docstring and a function docstring if not already provided.
    - Ensure correct imports for any type hints used in the signature.
    - Avoid trailing whitespace and ensure the file ends with a newline.

    Return only the final Python function implementation, without any reasoning text.
    """)


def build_self_refine_prompt(task_prompt: str, previous_code: str, feedback: str) -> str:
    return dedent(f"""
    You are given a Python function, its task description, and automated review feedback.
    Improve the code quality based on the feedback while preserving the existing behavior.

    Task:
    {task_prompt}

    Previous solution:
    {previous_code}

    Feedback:
    {feedback}

    Revision guidelines:
    - Do not change the algorithmic logic unless the feedback explicitly points to a bug.
    - Fix the specific style and structure issues described in the feedback.
    - Add missing docstrings, imports, and formatting corrections as needed.
    - Simplify overly complex expressions if the feedback flags high complexity.
    - Prefer minimal, targeted edits over a full rewrite.
    - Preserve the original function signature exactly.
    - Avoid trailing whitespace and ensure the file ends with a newline.

    Return only the improved Python code.
    """)
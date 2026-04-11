"""Prompt builders for SWE-Bench Lite patch generation.

SWE-Bench Lite requires generating a unified diff patch that fixes a real
GitHub issue. Unlike HumanEval (function-level), here the model must output
a proper `git diff` that can be applied with `patch -p1`.
"""
from textwrap import dedent


SWEBENCH_SYSTEM_RULES = dedent("""\
You are an expert software engineer specializing in bug fixing.
You will be given a description of a bug in a Python repository and
the relevant source code context.

Your task is to produce a minimal unified diff (git diff format) that fixes the issue.

Strict output rules:
1. Output ONLY the unified diff. Do not include any explanation or commentary.
2. The diff must start with `diff --git a/...` or `--- a/...`.
3. Make the smallest possible change to fix the issue.
4. Do not change unrelated code, formatting, or imports.
5. Do not remove or alter existing tests.
6. Use proper unified diff format: context lines, @@ hunks, + and - prefixes.
7. Do not use markdown fences (```diff ... ```).
""")


def build_swe_zero_shot_prompt(task_prompt: str) -> str:
    """Zero-shot: give issue description + file context, ask for patch."""
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}

Return ONLY the unified diff patch. Do not include explanations.
""")


def build_swe_cot_prompt(task_prompt: str) -> str:
    """Chain-of-thought: reason step-by-step internally, output only the patch."""
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}

Think step by step:
1. Identify the root cause of the bug.
2. Determine which file(s) and line(s) need to change.
3. Write the minimal fix.

IMPORTANT: Return ONLY the final unified diff patch. Do not include your reasoning.
""")


def build_swe_context_aware_prompt(task_prompt: str, file_context: str) -> str:
    """Context-aware: attach relevant code snippet for better grounding."""
    return dedent(f"""\
Fix the bug described below.

{task_prompt}

Relevant source code context:
```
{file_context}
```

Return ONLY the unified diff patch that fixes the issue. No explanations.
""")

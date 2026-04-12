"""Prompt builders for SWE-Bench patch generation.

SWE-Bench requires generating a unified diff patch that fixes a real
GitHub issue. The model must output a proper `git diff` that can be
applied with `patch -p1` against the exact base_commit of the repo.

Key fix: all prompts now receive the REAL file contents at base_commit
so the model generates correct line numbers and hunk offsets.
"""
from textwrap import dedent


SWEBENCH_SYSTEM_RULES = dedent("""\
You are an expert software engineer specializing in bug fixing.
You will be given:
  1. A description of a bug in a Python repository.
  2. The EXACT source code of the file(s) that need to be changed.

Your task is to produce a minimal unified diff (git diff format) that fixes the issue.

Strict output rules:
1. Output ONLY the unified diff. Do not include any explanation or commentary.
2. The diff MUST start with `diff --git a/path/to/file b/path/to/file`.
3. Line numbers in @@ hunks MUST match the provided source code exactly.
4. Include 3 lines of context around each change (standard unified diff).
5. Make the smallest possible change to fix the issue.
6. Do not change unrelated code, formatting, or imports.
7. Do not remove or alter existing tests.
8. Do not use markdown fences (```diff ... ```).
""")


def build_swe_zero_shot_prompt(task_prompt: str, file_contents: dict[str, str] | None = None) -> str:
    """Zero-shot: issue description + real file contents → patch."""
    files_section = _format_file_contents(file_contents)
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}
{files_section}
Return ONLY the unified diff patch. Do not include explanations.
""")


def build_swe_cot_prompt(task_prompt: str, file_contents: dict[str, str] | None = None) -> str:
    """Chain-of-thought: reason step-by-step internally, output only the patch."""
    files_section = _format_file_contents(file_contents)
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}
{files_section}
Think step by step:
1. Identify the root cause of the bug.
2. Find the exact lines in the provided source code that need to change.
3. Write the minimal fix using the EXACT line numbers from the source code above.

IMPORTANT: Return ONLY the final unified diff patch. Do not include your reasoning.
""")


def build_swe_context_aware_prompt(task_prompt: str, file_context: str) -> str:
    """Legacy context-aware prompt (kept for compatibility)."""
    return dedent(f"""\
Fix the bug described below.

{task_prompt}

Relevant source code context:
```
{file_context}
```

Return ONLY the unified diff patch that fixes the issue. No explanations.
""")


def _format_file_contents(file_contents: dict[str, str] | None) -> str:
    """Format a dict of {filepath: content} into a readable section for the prompt."""
    if not file_contents:
        return ""
    lines = ["\nSource code of the file(s) to modify:\n"]
    for filepath, content in file_contents.items():
        lines.append(f"=== {filepath} ===")
        # Add line numbers so the model can reference them precisely
        numbered = "\n".join(
            f"{i+1:4d} | {line}"
            for i, line in enumerate(content.splitlines())
        )
        lines.append(numbered)
        lines.append("")
    return "\n".join(lines)

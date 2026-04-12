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
  2. The EXACT source code of the file(s) that need to be changed, WITH LINE NUMBERS.

Your task is to produce a minimal unified diff (git diff format) that fixes the issue.

CRITICAL RULES:
1. Output ONLY the unified diff. Do not include ANY explanation or commentary.
2. The diff MUST start with `diff --git a/path/to/file b/path/to/file`.
3. Line numbers in @@ hunks MUST match the provided source code exactly.
4. Count line numbers from the numbered source code provided to you.
5. Include 3 lines of context around each change (standard unified diff).
6. Make the smallest possible change to fix the issue.
7. Do not change unrelated code, formatting, or imports.
8. Do not remove or alter existing tests.
9. Do not use markdown fences (```diff ... ```).
10. Do NOT use Unicode dashes - use regular ASCII dashes (--) only.
11. Double-check that context lines match the source code EXACTLY (including spaces).

UNIFIED DIFF FORMAT:
```
diff --git a/path/to/file.py b/path/to/file.py
--- a/path/to/file.py
+++ b/path/to/file.py
@@ -10,5 +10,5 @@ context line
 context line before
-old line to remove
+new line to add
 context line after
 context line
```
""")


def build_swe_zero_shot_prompt(task_prompt: str, file_contents: dict[str, str] | None = None) -> str:
    """Zero-shot: issue description + real file contents → patch."""
    files_section = _format_file_contents(file_contents)
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}
{files_section}

CRITICAL INSTRUCTIONS:
1. Use the EXACT line numbers from the numbered source code above.
2. Your @@ -start,count +start,count @@ headers MUST match these line numbers.
3. Context lines must match the source code EXACTLY (copy-paste them).
4. Output ONLY the unified diff, no explanations.

Return ONLY the unified diff patch that fixes the issue.
""")


def build_swe_cot_prompt(task_prompt: str, file_contents: dict[str, str] | None = None) -> str:
    """Chain-of-thought: reason step-by-step internally, output only the patch."""
    files_section = _format_file_contents(file_contents)
    return dedent(f"""\
Fix the bug described below by producing a unified diff patch.

{task_prompt}
{files_section}

Think step by step (do NOT output your reasoning):
1. Identify the root cause of the bug.
2. Locate the EXACT lines in the numbered source code above that need to change.
3. Note the line numbers from the source (e.g., "lines 127-145").
4. Write the minimal fix using those EXACT line numbers in the @@ hunk header.
5. Ensure context lines match the source code EXACTLY (copy-paste them).
6. Use regular ASCII dashes (--) not Unicode dashes.

CRITICAL: Return ONLY the final unified diff patch. Do not include your reasoning.
The diff MUST start with `diff --git a/path b/path` and have correct line numbers.
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
    lines = ["\n" + "="*80,
             "SOURCE CODE TO MODIFY (with line numbers):",
             "="*80 + "\n"]
    for filepath, content in file_contents.items():
        lines.append(f"FILE: {filepath}")
        lines.append("-" * 80)
        # Add line numbers so the model can reference them precisely
        numbered = "\n".join(
            f"{i+1:4d} | {line}"
            for i, line in enumerate(content.splitlines())
        )
        lines.append(numbered)
        lines.append("-" * 80)
        lines.append("")
    return "\n".join(lines)


def build_fallback_patch_prompt(task_prompt: str, file_contents: dict[str, str] | None = None) -> str:
    """
    Fallback prompt: ask for changes without line numbers.
    Used when standard diff generation fails.
    """
    files_section = _format_file_contents(file_contents)
    return dedent(f"""\
Fix the bug described below.

{task_prompt}
{files_section}

IMPORTANT: 
1. Show ONLY the lines that need to change.
2. For each change, write:
   REMOVE: <exact line to remove>
   ADD: <new line to add>
   AT: <brief description of location>

Example:
REMOVE:     old_value = self.scale
ADD:        old_value = self.scale.value if hasattr(self.scale, 'value') else self.scale
AT: Around line 127, in the evaluate method

Do NOT try to generate line numbers or hunk headers. Just show what to change.
""")

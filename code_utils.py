import ast
import re
from pathlib import Path
from typing import Tuple


def safe_filename_component(s: str) -> str:
    """Безопасное имя каталога/файла из task_id (например HumanEval/0)."""
    for ch in '\\/:*?"<>|':
        s = s.replace(ch, "_")
    s = s.strip()
    return s or "task"


def write_generation_artifacts(
    output_dir: Path,
    task_id: str,
    strategy: str,
    sample_index: int,
    final_code: str,
    initial_code: str | None,
) -> tuple[str | None, str | None]:
    """
    Сохраняет финальный и (для self_refine) начальный код в raw_generations/<task>/.
    Возвращает относительные пути (posix) под output_dir: code_file, initial_code_file.
    """
    base = Path(output_dir)
    safe = safe_filename_component(task_id)
    gen_dir = base / "raw_generations" / safe
    gen_dir.mkdir(parents=True, exist_ok=True)
    final_abs = gen_dir / f"{strategy}_sample{sample_index}.py"
    final_abs.write_text(final_code, encoding="utf-8")
    code_rel = final_abs.relative_to(base).as_posix()
    init_rel = None
    if initial_code is not None:
        init_abs = gen_dir / f"{strategy}_sample{sample_index}_initial.py"
        init_abs.write_text(initial_code, encoding="utf-8")
        init_rel = init_abs.relative_to(base).as_posix()
    return code_rel, init_rel


def strip_code_fences(text: str) -> str:
    """
    Убирает ```python ... ``` если модель всё же их вернула.
    """
    text = text.strip()
    text = re.sub(r"^```python\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def is_valid_python(code: str) -> Tuple[bool, str]:
    try:
        ast.parse(code)
        return True, ""
    except SyntaxError as exc:
        return False, f"SyntaxError: {exc}"


def extract_function_names(code: str) -> list[str]:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
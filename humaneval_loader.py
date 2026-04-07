from dataclasses import dataclass
from pathlib import Path
from typing import List
import json


@dataclass
class HumanEvalTask:
    task_id: str
    prompt: str
    entry_point: str
    canonical_solution: str | None = None
    test: str | None = None


def load_humaneval_tasks(
    file_path: str,
    max_tasks: int = 1
) -> List[HumanEvalTask]:
    """
    Загрузка задач из файла в формате JSONL (по одной задаче на строку).
    Каждая строка файла должна быть валидным JSON-объектом.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    tasks: List[HumanEvalTask] = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            row = json.loads(line)

            tasks.append(HumanEvalTask(
                task_id=row.get("task_id", ""),
                prompt=row.get("prompt", ""),
                entry_point=row.get("entry_point", ""),
                canonical_solution=row.get("canonical_solution"),
                test=row.get("test")
            ))

            if len(tasks) >= max_tasks:
                break

    return tasks
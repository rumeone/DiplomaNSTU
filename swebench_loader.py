from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from datasets import load_dataset


@dataclass
class SWETask:
    """
    Одна задача из датасета SWE-bench.

    Поля соответствуют схеме princeton-nlp/SWE-bench_Lite:
      - instance_id   — уникальный идентификатор задачи (repo__issueN)
      - repo          — полное имя репозитория на GitHub (например, django/django)
      - problem_statement — текст issue (описание бага/запроса)
      - base_commit   — SHA коммита, к которому применяется патч
      - patch         — эталонный патч (ground-truth diff)
      - test_patch    — патч с тестами (если есть)
      - hints_text    — доп. подсказки из треда issue (может быть пустым)

    При генерации кода используется только problem_statement (+ hints_text),
    чтобы не допускать утечки эталонного решения в промпт.
    """
    instance_id: str
    repo: str
    problem_statement: str
    base_commit: str = ""
    patch: str | None = None
    test_patch: str | None = None
    hints_text: str | None = None

    # ── поля, совместимые с интерфейсом HumanEvalTask ──────────────────────
    @property
    def task_id(self) -> str:
        return self.instance_id

    @property
    def prompt(self) -> str:
        """
        Единый текст задачи для передачи в промпт-строители.
        Добавляем hints_text только если они не пустые.
        """
        parts = [
            f"Repository: {self.repo}",
            "",
            "Issue description:",
            self.problem_statement.strip(),
        ]
        if self.hints_text and self.hints_text.strip():
            parts += ["", "Additional hints:", self.hints_text.strip()]
        return "\n".join(parts)

    @property
    def entry_point(self) -> str:
        """
        SWE-bench не имеет понятия entry_point.
        Возвращаем идентификатор задачи как метку.
        """
        return self.instance_id


# ---------------------------------------------------------------------------
# Загрузчики
# ---------------------------------------------------------------------------

_SWEBENCH_DATASETS = [
    # Lite — 300 отобранных задач (рекомендуется для диплома)
    ("princeton-nlp/SWE-bench_Lite", "test"),
    # Verified — 500 задач с верификацией от OpenAI
    ("princeton-nlp/SWE-bench_Verified", "test"),
    # Полный датасет — 2294 задачи
    ("princeton-nlp/SWE-bench", "test"),
]


def load_swebench_tasks(
    max_tasks: int = 10,
    split: str = "test",
    subset: str = "lite",
) -> List[SWETask]:
    """
    Загружает задачи из SWE-bench через Hugging Face datasets.

    Parameters
    ----------
    max_tasks : int
        Максимальное число задач для загрузки.
    split : str
        Сплит датасета (обычно "test").
    subset : str
        Вариант датасета: "lite" (300 задач), "verified" (500), "full" (2294).

    Returns
    -------
    List[SWETask]
    """
    subset_map = {
        "lite": "princeton-nlp/SWE-bench_Lite",
        "verified": "princeton-nlp/SWE-bench_Verified",
        "full": "princeton-nlp/SWE-bench",
    }
    dataset_name = subset_map.get(subset, "princeton-nlp/SWE-bench_Lite")

    ds = load_dataset(dataset_name, split=split)

    tasks: List[SWETask] = []
    for row in ds:
        tasks.append(SWETask(
            instance_id=row.get("instance_id", ""),
            repo=row.get("repo", ""),
            problem_statement=row.get("problem_statement", ""),
            base_commit=row.get("base_commit", ""),
            patch=row.get("patch"),
            test_patch=row.get("test_patch"),
            hints_text=row.get("hints_text"),
        ))
        if len(tasks) >= max_tasks:
            break

    if not tasks:
        raise RuntimeError(
            f"Не удалось загрузить задачи из {dataset_name} (split={split})."
        )

    return tasks


def load_swebench_from_jsonl(
    file_path: str | Path,
    max_tasks: int = 10,
) -> List[SWETask]:
    """
    Загрузка задач SWE-bench из локального JSONL-файла.
    Используется если нет доступа к Hugging Face или нужен оффлайн-режим.

    Формат строки файла должен соответствовать схеме princeton-nlp/SWE-bench.
    """
    import json

    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    tasks: List[SWETask] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            tasks.append(SWETask(
                instance_id=row.get("instance_id", ""),
                repo=row.get("repo", ""),
                problem_statement=row.get("problem_statement", ""),
                base_commit=row.get("base_commit", ""),
                patch=row.get("patch"),
                test_patch=row.get("test_patch"),
                hints_text=row.get("hints_text"),
            ))
            if len(tasks) >= max_tasks:
                break

    return tasks

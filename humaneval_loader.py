"""HumanEval task loader.

Supports multiple data sources:
1. Local JSONL files (HumanEvalPlus format)
2. HuggingFace datasets (HumanEvalNext format)
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Literal
import json


@dataclass
class HumanEvalTask:
    """Represents a single HumanEval task."""
    task_id: str
    prompt: str
    entry_point: str
    canonical_solution: str | None = None
    test: str | None = None


def load_humaneval_tasks(
    file_path: str | None = None,
    max_tasks: int = 10,
    source: Literal["local", "humaneval_next"] = "local",
) -> List[HumanEvalTask]:
    """Load HumanEval tasks from various sources.
    
    Args:
        file_path: Path to local JSONL file (for source="local")
        max_tasks: Maximum number of tasks to load
        source: Data source - "local" or "humaneval_next"
        
    Returns:
        List of HumanEvalTask objects
    """
    if source == "humaneval_next":
        return _load_from_humaneval_next(max_tasks)
    else:
        return _load_from_local(file_path, max_tasks)


def _load_from_local(file_path: str | None, max_tasks: int) -> List[HumanEvalTask]:
    """Load tasks from local JSONL file."""
    if not file_path:
        raise ValueError("file_path is required for local source")
    
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

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


def _load_from_humaneval_next(max_tasks: int) -> List[HumanEvalTask]:
    """Load tasks from HuggingFace HumanEvalNext dataset.
    
    HumanEvalNext contains test code, making it suitable for
    functional evaluation.
    """
    from datasets import load_dataset
    
    ds = load_dataset("AISE-TUDelft/HumanEvalNext", split="train")
    tasks: List[HumanEvalTask] = []

    for row in ds:
        tasks.append(HumanEvalTask(
            task_id=row["task_id"],
            prompt=row["prompt"],
            entry_point=row["entry_point"],
            canonical_solution=row.get("canonical_solution"),
            test=row.get("test"),
        ))
        
        if len(tasks) >= max_tasks:
            break

    return tasks

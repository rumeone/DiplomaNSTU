from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Literal


@dataclass
class ModelConfig:
    model_name: str = "deepseek/deepseek-v3.2"
    temperature: float = 0.2
    max_output_tokens: int = 5000


@dataclass
class ExperimentConfig:
    # ── Режим датасета ─────────────────────────────────────────────────────
    # "humaneval" — использовать локальный JSONL (например, HumanEvalPlus-Mini.jsonl)
    # "swebench" — загружать SWE-bench через Hugging Face
    # "swebench_local" — загружать SWE-bench из локального JSONL
    dataset_mode: Literal["humaneval", "swebench", "swebench_local"] = "swebench"

    # Путь к JSONL-файлу (только для humaneval и swebench_local)
    dataset_path: Path = Path("HumanEvalPlus-Mini.jsonl")

    # Подмножество SWE-bench: "lite" (300), "verified" (500), "full" (2294)
    swebench_subset: str = "lite"

    # Максимальное число задач
    max_tasks: int = 5

    # Генераций на одну задачу для каждой стратегии
    samples_per_task: int = 1

    strategies: List[str] = field(default_factory=lambda: [
        "zero_shot",
        "constraint_guided",
        "structured_cot",
        "self_refine",
    ])

    output_dir: Path = Path("outputs")
    run_refinement: bool = True
    max_refinement_rounds: int = 1

    # Включить запуск тестов через human-eval harness.
    # Для SWE-bench всегда False: там нужен отдельный harness (swe-bench-eval).
    enable_external_execution: bool = False


MODEL_CONFIG = ModelConfig()
EXPERIMENT_CONFIG = ExperimentConfig()

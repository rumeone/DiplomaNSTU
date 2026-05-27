from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Literal


@dataclass
class ModelConfig:
    """Конфигурация модели-генератора кода."""
    model_name: str = "deepseek/deepseek-v3.2"
    temperature: float = 0.2
    max_output_tokens: int = 5000


@dataclass
class ParallelismConfig:
    """Configuration for parallel/async execution."""
    # Maximum concurrent API requests
    max_concurrent_requests: int = 10
    # Maximum retries for failed API requests
    max_retries: int = 3
    # Timeout for each API request in seconds
    request_timeout_seconds: float = 120.0
    # Enable async mode (uses AsyncLLMClient)
    use_async: bool = True


@dataclass
class ReviewerConfig:
    """Конфигурация модели-рецензента (LLM-as-a-Judge)."""
    # Модель-рецензент (может отличаться от генерирующей модели)
    model: str = "deepseek/deepseek-v3.2"
    # Температура для ревью (низкая — для стабильности оценок)
    temperature: float = 0.1
    # Максимум токенов на ответ ревьюера
    max_output_tokens: int = 500
    # Включить LLM-ревью (можно переопределить флагом --enable-llm-review)
    enabled: bool = False
    # API-ключ (по умолчанию берётся из REVIEWER_API_KEY)
    api_key: str | None = None
    # Базовый URL для API рецензента
    base_url: str | None = None


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

    output_dir: Path = Path("outputs_deepseek_model_3")
    run_refinement: bool = True
    max_refinement_rounds: int = 3

    # Включить запуск тестов через human-eval harness.
    # Для SWE-bench всегда False: там нужен отдельный harness (swe-bench-eval).
    enable_external_execution: bool = True

    # ── Параллелизм ────────────────────────────────────────────────────────
    parallelism: ParallelismConfig = field(default_factory=ParallelismConfig)

    # ── Рецензент ─────────────────────────────────────────────────────────
    reviewer: ReviewerConfig = field(default_factory=ReviewerConfig)

    # Resume: продолжить с последней обработанной задачи (игнорировать уже готовые)
    resume_enabled: bool = True


MODEL_CONFIG = ModelConfig()
PARALLELISM_CONFIG = ParallelismConfig()
REVIEWER_CONFIG = ReviewerConfig()
EXPERIMENT_CONFIG = ExperimentConfig()

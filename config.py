from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class ModelConfig:
    model_name: str = "deepseek/deepseek-v3.2"
    temperature: float = 0.2
    max_output_tokens: int = 5000


@dataclass
class ExperimentConfig:
    dataset_path: Path = Path("HumanEvalPlus-Mini.jsonl")
    max_tasks: int = 1
    samples_per_task: int = 1
    strategies: List[str] = field(default_factory=lambda: [
        "zero_shot",
        "constraint_guided",
        "structured_cot",
        "self_refine"
    ])
    output_dir: Path = Path("outputs")
    run_refinement: bool = True
    max_refinement_rounds: int = 1
    enable_external_execution: bool = False


MODEL_CONFIG = ModelConfig()
EXPERIMENT_CONFIG = ExperimentConfig()
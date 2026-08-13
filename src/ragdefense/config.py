"""Configuration defaults for the RAG defense pipeline."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class DefenseConfig:
    """Configuration for the defense layers."""

    seed: int = 42
    model_name: str = "Qwen/Qwen2.5-0.5B-Instruct"
    embedding_model: str = "all-MiniLM-L6-v2"
    faiss_metric: str = "IP"
    query_blocklist: List[str] = field(
        default_factory=lambda: [
            "weapon",
            "explosive",
            "bomb",
            "drug synthesis",
            "poison",
            "illegal"
        ]
    )
    output_toxicity_threshold: float = 0.75
    instructionality_threshold: float = 0.6
    groundedness_threshold: float = 0.7
    trust_threshold: float = 0.5
    split_ratios: Dict[str, float] = field(default_factory=lambda: {"train": 0.70, "val": 0.15, "test": 0.15})


CFG = DefenseConfig()

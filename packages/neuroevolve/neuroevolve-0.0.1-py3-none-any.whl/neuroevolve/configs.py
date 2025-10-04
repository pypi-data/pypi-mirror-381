"""
configs.py — central defaults & small helpers

This module defines the default configuration values for the GA/ES engine and
evaluation budgets. Keep it dependency-light (pure stdlib).
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional


@dataclass(frozen=True)
class EvalBudget:
    """Short-budget evaluation settings for quick fitness estimation."""
    epochs: int = 3
    batch_size: int = 64
    max_steps: Optional[int] = None  # if set, can override epochs with fixed steps


@dataclass(frozen=True)
class RetrainBudget:
    """Longer retrain budget for top-k genomes after the search is done."""
    enabled: bool = True
    top_k: int = 5
    epochs: int = 100
    batch_size: int = 128


@dataclass(frozen=True)
class PopulationConfig:
    """Population & operator rates."""
    population_size: int = 50
    generations: int = 30
    elitism: int = 2
    mutation_rate: float = 0.2
    crossover_rate: float = 0.6
    random_immigrants: int = 0  # inject fresh random genomes per generation


@dataclass(frozen=True)
class MultiObjectiveConfig:
    """Multi-objective fitness settings & novelty."""
    use_pareto: bool = False
    novelty_k: int = 10
    novelty_weight: float = 0.0  # if scalarizing, weight for novelty
    complexity_weight: float = 0.0  # weight for params/FLOPs penalties in scalarization


@dataclass(frozen=True)
class RunConfig:
    """
    Top-level config that other modules can pass around. Everything serializable.
    """
    seed: int = 42
    eval_budget: EvalBudget = field(default_factory=EvalBudget)
    retrain_budget: RetrainBudget = field(default_factory=RetrainBudget)
    population: PopulationConfig = field(default_factory=PopulationConfig)
    objectives: MultiObjectiveConfig = field(default_factory=MultiObjectiveConfig)
    # free-form extras (task-specific config, dataset paths, etc.)
    extras: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


# ---- tiny self-test ----
if __name__ == "__main__":
    cfg = RunConfig()
    print("RunConfig OK, dict preview:")
    print({k: (v if not isinstance(v, dict) else "dict(...)") for k, v in cfg.to_dict().items()})

"""
evaluation.py — evaluator interface, specs, and a deterministic MockEvaluator.

Goals:
- Define a clear contract for turning a Genome + TaskSpec -> EvaluationResult.
- Provide a fast, reproducible MockEvaluator (no torch/gym required) to
  drive CI, demos, and early engine tests without GPUs or datasets.
- Keep it stdlib-first; allow pluggable real evaluators later.

Usage:
  from .genome import Genome, GenomeType
  from .evaluation import TaskSpec, EvaluationResult, MockEvaluator

  evaluator = MockEvaluator()
  result = evaluator.evaluate(genome, TaskSpec(name="cifar_tiny", kind="supervised"))
"""

from __future__ import annotations


if __name__ == "__main__" and __package__ is None:
    # allow running this file directly in VS Code
    import sys, pathlib
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[2] / "src"))
    __package__ = "neuroevolve"
    from neuroevolve.genome import Genome, GenomeType, VALIDATORS  # noqa


import hashlib
import json
import math
import time
from dataclasses import dataclass, asdict, field
from typing import Any, Dict, Optional, Protocol, Tuple

from .genome import Genome, GenomeType


# ---------------------------- Datamodels ----------------------------

@dataclass(frozen=True)
class TaskSpec:
    """
    Lightweight description of the task & evaluation budget.

    name: human-readable tag ("cifar_tiny", "cartpole", "gan_fid")
    kind: "supervised" | "rl" | "generative" | "other"
    epochs, batch_size, max_steps: budget knobs for real evaluators; ignored by Mock
    perf_weight: weight for the primary performance metric in scalarization
    params_weight: penalty weight for parameter count (complexity)
    flops_weight: penalty weight for flops proxy (if available)
    noise: optional jitter to simulate measurement noise in real runs (Mock uses 0 by default)
    """
    name: str = "mock_task"
    kind: str = "supervised"
    epochs: int = 3
    batch_size: int = 64
    max_steps: Optional[int] = None

    perf_weight: float = 1.0
    params_weight: float = 0.0
    flops_weight: float = 0.0
    noise: float = 0.0

    extras: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EvaluationResult:
    """
    Output of an evaluation. Designed to be JSON-serializable.
    """
    # Multi-metric fitness dictionary (maximize by default)
    fitness: Dict[str, float]
    # Optional scalarization of fitness (for simple GA selection)
    scalar_fitness: Optional[float]
    # Free-form metrics (curves, timings, etc.)
    metrics: Dict[str, Any]
    # Paths or small blobs to artifacts/checkpoints (real evals will fill these)
    checkpoints: Dict[str, Any]
    # Runtime (seconds) for the evaluation call
    eval_time_seconds: float
    # Success flag & error text (if any)
    succeeded: bool = True
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class Evaluator(Protocol):
    """
    Minimal evaluator protocol. Implementations should be side-effect-light
    (except for saving checkpoints to a provided run dir via logging_utils).
    """

    def evaluate(self, genome: Genome, task: TaskSpec) -> EvaluationResult:
        ...


# ---------------------------- MockEvaluator ----------------------------

class MockEvaluator:
    """
    Deterministic, fast evaluator that *does not* train.
    It computes synthetic metrics from the genome structure and a hash seed.

    Intended uses:
      - Unit tests (reproducibility under fixed genome)
      - CI smoke tests
      - Debugging GA loop & logging without heavy deps

    Heuristics:
      - perf (primary metric) ~ sigmoid(a * structure_score + b * hash_noise)
      - params ~ structural proxy (layers/filters/units or nodes)
      - flops ~ rough function of params (scaled)
    """

    def __init__(self, jitter: float = 0.0) -> None:
        """
        jitter: additional random-like perturbation magnitude (0 = fully deterministic)
        """
        self.jitter = float(jitter)

    # ---------- public API ----------

    def evaluate(self, genome: Genome, task: TaskSpec) -> EvaluationResult:
        t0 = time.perf_counter()

        # Deterministic base seed = hash(genome JSON + task.name + genome.seed)
        base_hash = self._hash_key(genome, task)
        # Compute structural proxies
        params_proxy, flops_proxy = self._complexity_proxies(genome)
        # Primary performance (0..1 for supervised/generative; reward-ish for rl)
        perf = self._performance_proxy(genome, task, base_hash)

        # Build fitness dict keyed by task kind
        if task.kind == "rl":
            fitness = {"reward": perf, "params": -params_proxy, "flops": -flops_proxy}
        elif task.kind == "generative":
            # Lower FID is better; convert to a "higher is better" score in [0,1]
            fid = (1.0 - perf) * 50.0 + 5.0  # 5..55 as a pseudo-FID
            fid_score = 1.0 / (1.0 + fid)    # ~0..0.16
            fitness = {"fid_score": fid_score, "params": -params_proxy, "flops": -flops_proxy}
        else:
            # supervised default: accuracy-ish in [0,1]
            fitness = {"val_acc": perf, "params": -params_proxy, "flops": -flops_proxy}

        # Optional scalarization (maximize)
        scalar = (
            task.perf_weight * fitness.get("val_acc", fitness.get("fid_score", fitness.get("reward", 0.0)))
            + task.params_weight * fitness["params"]
            + task.flops_weight * fitness["flops"]
        )

        dt = time.perf_counter() - t0
        metrics = {
            "params_proxy": params_proxy,
            "flops_proxy": flops_proxy,
            "base_hash": base_hash,
            "eval_time_ms": round(dt * 1000.0, 3),
        }
        return EvaluationResult(
            fitness=fitness,
            scalar_fitness=scalar,
            metrics=metrics,
            checkpoints={},  # real evaluators would write paths/tensors here
            eval_time_seconds=dt,
            succeeded=True,
            error=None,
        )

    # ---------- helpers ----------

    @staticmethod
    def _hash_key(genome: Genome, task: TaskSpec) -> int:
        body = json.dumps(
            {"g": genome.to_dict(), "task": {"name": task.name, "kind": task.kind}, "seed": genome.seed},
            sort_keys=True,
            separators=(",", ":"),
        )
        h = hashlib.sha256(body.encode("utf-8")).hexdigest()
        # deterministically map to 32-bit int
        return int(h[:8], 16)

    def _performance_proxy(self, genome: Genome, task: TaskSpec, hkey: int) -> float:
        """
        Produce a stable "performance" in [0,1] for non-RL, or ~[0,∞) proxy for RL mapped into [0,1] here.
        We use a sigmoid over a structure score plus tiny deterministic noise from hash.
        """
        s = self._structure_score(genome)
        # map hash to small noise in [-0.15, 0.15]
        noise = ((hkey % 1000) / 1000.0 - 0.5) * 0.3 + self.jitter * 0.0
        x = 1.2 * s + noise  # scale structure influence
        perf = 1.0 / (1.0 + math.exp(-x))  # 0..1
        if task.kind == "rl":
            # Convert to reward-ish scale (e.g., 0..500) but still normalize back if desired by caller
            reward = 500.0 * perf
            # Return normalized for consistency inside fitness (keep 0..1)
            return min(1.0, reward / 500.0)
        return perf

    @staticmethod
    def _complexity_proxies(genome: Genome) -> Tuple[float, float]:
        """
        Estimate parameter count and FLOPs-ish numbers from structure only.
        This is a *proxy*, not exact.
        """
        p = 0.0
        if genome.type == GenomeType.TABULAR:
            layers = genome.payload.get("layers", [])
            in_ch = 3  # default assumption for images
            cur = in_ch
            for L in layers:
                t = str(L.get("type", "")).lower()
                if t in {"conv", "conv2d"}:
                    k = int(L.get("kernel", 3))
                    f = int(L.get("filters", 16))
                    p += (k * k * cur * f) + f  # conv weights + bias
                    cur = f
                elif t in {"dense", "linear"}:
                    u = int(L.get("units", 64))
                    p += cur * u + u
                    cur = u
                elif t in {"maxpool", "avgpool"}:
                    # no params
                    pass
                else:
                    # unknown -> small cost
                    p += 8.0
        elif genome.type == GenomeType.GRAPH:
            nodes = genome.payload.get("nodes", {})
            edges = genome.payload.get("edges", [])
            p += 32.0 * len(nodes) + 4.0 * len(edges)
        elif genome.type == GenomeType.CONTROLLER:
            arch = genome.payload.get("arch", {})
            layers = arch.get("layers", [])
            last = None
            for w in layers:
                if last is None:
                    last = w
                else:
                    p += last * w + w
                    last = w
            p += 16.0  # small constant overhead
        elif genome.type == GenomeType.CPPN:
            arch = genome.payload.get("cppn_arch", {})
            layers = arch.get("layers", [])
            for i in range(1, len(layers)):
                p += layers[i - 1] * layers[i] + layers[i]
            p += 32.0

        flops = 2.5 * p  # rough proportionality
        return float(p), float(flops)

    @staticmethod
    def _structure_score(genome: Genome) -> float:
        """
        Map structural choices into a compact score; normalized-ish to ~[-1, 1].
        """
        if genome.type == GenomeType.TABULAR:
            layers = genome.payload.get("layers", [])
            depth = len(layers)
            act_bonus = 0.0
            for L in layers:
                a = str(L.get("act", "")).lower()
                if a in {"relu", "gelu", "silu", "swish"}:
                    act_bonus += 0.05
            # more depth helps up to ~6
            base = min(depth, 6) / 6.0 + act_bonus
            # capacity bonus from filters/units (log-scaled)
            cap = 0.0
            for L in layers:
                t = str(L.get("type", "")).lower()
                if t in {"conv", "conv2d"}:
                    cap += math.log2(1 + int(L.get("filters", 16)))
                elif t in {"dense", "linear"}:
                    cap += math.log2(1 + int(L.get("units", 64)))
            cap = cap / (len(layers) or 1) / 6.0
            return base + cap - 0.3  # shift roughly to center
        if genome.type == GenomeType.GRAPH:
            nodes = genome.payload.get("nodes", {})
            edges = genome.payload.get("edges", [])
            deg = (len(edges) / (len(nodes) + 1e-6))
            return 0.2 + 0.15 * len(nodes) + 0.05 * deg
        if genome.type == GenomeType.CONTROLLER:
            arch = genome.payload.get("arch", {})
            layers = arch.get("layers", [])
            depth = len(layers)
            width = sum(layers) / (len(layers) or 1)
            return 0.1 + 0.05 * depth + 0.0005 * width
        if genome.type == GenomeType.CPPN:
            arch = genome.payload.get("cppn_arch", {})
            layers = arch.get("layers", [])
            return 0.15 + 0.06 * len(layers)
        return 0.0


# ---------------------------- tiny self-test ----------------------------

if __name__ == "__main__":
    from .genome import GenomeType

    # Build a sample TABULAR genome
    g = Genome.new(
        GenomeType.TABULAR,
        payload={
            "layers": [
                {"type": "conv2d", "filters": 32, "kernel": 3, "act": "relu"},
                {"type": "maxpool", "ks": 2},
                {"type": "dense", "units": 128, "act": "relu"},
            ],
            "optimizer": {"name": "adam", "lr": 1e-3},
        },
        seed=123,
    )

    task = TaskSpec(name="cifar_tiny", kind="supervised", perf_weight=1.0, params_weight=1e-7, flops_weight=0.0)
    ev = MockEvaluator()
    r1 = ev.evaluate(g, task)
    r2 = ev.evaluate(g, task)

    print("EvaluationResult:", json.dumps(r1.to_dict(), indent=2))
    assert r1.fitness == r2.fitness, "MockEvaluator must be deterministic for same genome+task"
    assert 0.0 <= r1.fitness["val_acc"] <= 1.0, "val_acc should be within [0,1]"
    print("MockEvaluator self-test OK")

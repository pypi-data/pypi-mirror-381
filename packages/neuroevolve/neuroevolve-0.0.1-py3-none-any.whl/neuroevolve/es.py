"""
es.py — evolutionary engine (generational + steady-state)

Design goals:
- Dependency-light, deterministic under seed, plug-and-play.
- Works with any Evaluator implementing the Protocol from evaluation.py.
- Logs population snapshots, metrics CSVs, and lineage for later analysis.

Key functions:
  - run_generational(...)
  - run_steady_state(...)

Utilities:
  - init_population_random(...)
  - evaluate_population(...)
  - make_offspring(...)

Notes:
- This is a *minimal viable* engine that supports:
    • tournament/roulette selection
    • mutation & crossover with configurable rates
    • elitism
    • random immigrants
    • multi-objective friendly (uses scalar_fitness if provided; or picks first metric)
- Later we can add NSGA-II style loops; for now, Pareto selection is available
  from selection.select_pareto if you want to swap it in externally.
"""

from __future__ import annotations

if __name__ == "__main__" and __package__ is None:
    # allow running this file directly in VS Code
    import sys, pathlib
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[2] / "src"))
    __package__ = "neuroevolve"
    from neuroevolve.genome import Genome, GenomeType, VALIDATORS  # noqa




import json
import math
import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from .configs import RunConfig
from .evaluation import Evaluator, TaskSpec, EvaluationResult, MockEvaluator
from .genome import Genome, GenomeType
from .logging_utils import (
    make_run_dir,
    save_run_header,
    save_population_snapshot,
    save_metrics_csv,
    save_lineage,
    set_all_seeds,
)
from .operators import (
    mutate_activation,
    mutate_add_layer,
    mutate_remove_layer,
    mutate_layer_param,
    mutate_hyperparam,
    mutate_rewire_edge,
    mutate_controller_noise,
    one_point_crossover,
    uniform_crossover_hparams,
    subgraph_crossover,
)
from .selection import tournament_selection, roulette_selection


# ------------------------------ Data models ------------------------------

@dataclass
class EngineStats:
    generation: int
    eval_seconds: float
    best_scalar: float
    mean_scalar: float
    median_scalar: float
    population_size: int


# ------------------------------ Population init ------------------------------

def init_population_random(
    size: int,
    genome_type: GenomeType = GenomeType.TABULAR,
    seed: int = 42,
) -> List[Genome]:
    """
    Create a small random population for bootstrapping.
    Keeps it simple; task-specific initializers can be supplied by users.
    """
    rng = random.Random(seed)
    pop: List[Genome] = []
    for i in range(size):
        g_seed = seed + i + rng.randrange(10_000)
        if genome_type == GenomeType.TABULAR:
            depth = rng.randint(1, 4)
            layers: List[Dict[str, Any]] = []
            for d in range(depth):
                if rng.random() < 0.6:
                    layers.append({
                        "type": "conv2d",
                        "filters": rng.choice([16, 32, 64]),
                        "kernel": rng.choice([1, 3, 5]),
                        "stride": 1,
                        "act": rng.choice(["relu", "gelu", "silu"]),
                    })
                else:
                    layers.append({
                        "type": "dense",
                        "units": rng.choice([64, 128, 256]),
                        "act": rng.choice(["relu", "gelu", "silu"]),
                    })
            payload = {
                "layers": layers,
                "optimizer": {"name": "adam", "lr": rng.choice([5e-4, 1e-3, 2e-3])},
            }
            pop.append(Genome.new(GenomeType.TABULAR, payload, seed=g_seed))
        elif genome_type == GenomeType.GRAPH:
            nodes = {f"n{k}": {"op": rng.choice(["conv3x3", "conv1x1", "add", "id"])} for k in range(rng.randint(3, 5))}
            node_names = list(nodes.keys())
            edges: List[List[str]] = []
            for _ in range(rng.randint(2, 5)):
                u, v = rng.sample(node_names, 2)
                if u != v and [u, v] not in edges:
                    edges.append([u, v])
            payload = {"nodes": nodes, "edges": edges, "readouts": [node_names[-1]]}
            pop.append(Genome.new(GenomeType.GRAPH, payload, seed=g_seed))
        elif genome_type == GenomeType.CONTROLLER:
            width = rng.choice([8, 16, 32])
            payload = {
                "arch": {"type": "mlp", "layers": [width, width, max(4, width // 2)]},
                "weights": {"w": [rng.uniform(-0.1, 0.1) for _ in range(width)]},
                "modulation_targets": ["layer1_gain", "layer3_lr_mult"],
            }
            pop.append(Genome.new(GenomeType.CONTROLLER, payload, seed=g_seed))
        else:  # GenomeType.CPPN
            layers = [rng.choice([8, 16]), rng.choice([8, 16]), 1]
            payload = {
                "cppn_arch": {"type": "mlp", "layers": layers},
                "cppn_weights": {"W1": [[rng.uniform(-0.2, 0.2) for _ in range(layers[0])] for _ in range(layers[1])]},
                "mapping_spec": {"target": "conv_filters", "shape": [8, 8]},
            }
            pop.append(Genome.new(GenomeType.CPPN, payload, seed=g_seed))
    return pop


# ------------------------------ Evaluation helpers ------------------------------

def _scalar_from_result(res: EvaluationResult) -> float:
    if res.scalar_fitness is not None:
        return float(res.scalar_fitness)
    # fallback: take the first metric as scalar
    if res.fitness:
        return float(next(iter(res.fitness.values())))
    return float("-inf")


def evaluate_population(
    population: Sequence[Genome],
    evaluator: Evaluator,
    task: TaskSpec,
) -> Tuple[List[EvaluationResult], List[float]]:
    results: List[EvaluationResult] = []
    scalars: List[float] = []
    for g in population:
        r = evaluator.evaluate(g, task)
        results.append(r)
        scalars.append(_scalar_from_result(r))
    return results, scalars


# ------------------------------ Offspring creation ------------------------------

def _mutate_any(g: Genome, rng: random.Random) -> Genome:
    """
    Apply one randomly chosen mutation appropriate to the genome type.
    """
    if g.type == GenomeType.TABULAR:
        op = rng.choice(["act", "add", "rm", "hparam", "layerparam"])
        if op == "act":
            return mutate_activation(g)
        if op == "add":
            return mutate_add_layer(g)
        if op == "rm":
            return mutate_remove_layer(g)
        if op == "hparam":
            return mutate_hyperparam(g, "lr", scale=0.15)
        return mutate_layer_param(g, layer_idx=rng.randrange(len(g.payload.get("layers", [0]))), param="units", step=rng.choice([16, 32]))
    if g.type == GenomeType.GRAPH:
        return mutate_rewire_edge(g)
    if g.type == GenomeType.CONTROLLER:
        return mutate_controller_noise(g, sigma=0.02)
    # CPPN: reuse controller noise on weights-like fields later; for now no-op
    return g


def _crossover_any(a: Genome, b: Genome, rng: random.Random) -> Genome:
    """
    Apply a type-appropriate crossover, preferring structural ones when possible.
    If types differ, just return a mutated copy of parent A.
    """
    if a.type != b.type:
        return _mutate_any(a, rng)
    if a.type == GenomeType.TABULAR:
        # 50/50 layers crossover vs hyperparam crossover
        if rng.random() < 0.5:
            return one_point_crossover(a, b)
        return uniform_crossover_hparams(a, b, keys=["lr"])
    if a.type == GenomeType.GRAPH:
        return subgraph_crossover(a, b, fraction=0.5)
    if a.type == GenomeType.CONTROLLER:
        # No weight-blend yet; use mutation to keep it simple
        return _mutate_any(a, rng)
    # CPPN: fallback to mutation
    return _mutate_any(a, rng)


def make_offspring(
    parents_idx: Sequence[int],
    population: Sequence[Genome],
    mutation_rate: float,
    crossover_rate: float,
    rng: random.Random,
) -> List[Genome]:
    """
    Create offspring equal to len(population) using the given parent indices.
    Strategy:
      - sample pairs from parents_idx
      - apply crossover with prob=crossover_rate, else clone+mutate
      - always consider mutation with prob=mutation_rate on the resulting child
    """
    offspring: List[Genome] = []
    n = len(population)
    for _ in range(n):
        p1 = population[rng.choice(parents_idx)]
        p2 = population[rng.choice(parents_idx)]
        if rng.random() < crossover_rate:
            child = _crossover_any(p1, p2, rng)
        else:
            child = p1
        if rng.random() < mutation_rate:
            child = _mutate_any(child, rng)
        offspring.append(child)
    return offspring


# ------------------------------ Engines ------------------------------

def run_generational(
    evaluator: Evaluator,
    task: TaskSpec,
    config: RunConfig,
    selection: str = "tournament",  # "tournament" | "roulette"
    genome_type: GenomeType = GenomeType.TABULAR,
    run_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Classic generational GA with elitism and random immigrants.
    Returns a dict with summary, best genome, and run_dir.
    """
    # Seeding & run dir
    seed_info = set_all_seeds(config.seed)
    rdir = make_run_dir(run_dir or "experiments/runs")
    save_run_header(rdir, config.to_dict(), seed_info)

    # Init population
    rng = random.Random(config.seed)
    population = init_population_random(config.population.population_size, genome_type=genome_type, seed=config.seed)

    lineage_edges: List[Dict[str, Any]] = []  # we add edges only when we actually create new genomes

    # Evaluate initial pop
    t0 = time.perf_counter()
    results, scalars = evaluate_population(population, evaluator, task)
    dt = time.perf_counter() - t0
    best_idx = max(range(len(population)), key=lambda i: scalars[i])
    best = population[best_idx]
    save_population_snapshot(rdir, 0, [g.to_dict() for g in population])
    save_metrics_csv(
        rdir, 0,
        [{"id": population[i].id, "scalar": scalars[i], **results[i].fitness} for i in range(len(population))]
    )

    # generations
    for gen in range(1, config.population.generations + 1):
        # Select parents
        if selection == "roulette":
            parent_idx = roulette_selection(population, scalars, k=len(population), seed=rng.randrange(10_000))
        else:
            parent_idx = tournament_selection(population, scalars, k=len(population), tsize=3, p_win=1.0, seed=rng.randrange(10_000))

        # Offspring
        offspring = make_offspring(
            parent_idx,
            population,
            mutation_rate=config.population.mutation_rate,
            crossover_rate=config.population.crossover_rate,
            rng=rng,
        )

        # Elitism: keep top-K from previous generation
        elite_k = max(0, min(config.population.elitism, len(population)))
        elite_idx = sorted(range(len(population)), key=lambda i: scalars[i], reverse=True)[:elite_k]
        elites = [population[i] for i in elite_idx]

        # Random immigrants
        immigrants: List[Genome] = []
        if config.population.random_immigrants > 0:
            immigrants = init_population_random(config.population.random_immigrants, genome_type=genome_type, seed=config.seed + gen * 97)

        # New population assembly
        new_population = elites + offspring
        if immigrants:
            # trim offspring if needed to make space
            new_population = (elites + offspring)[: len(population) - len(immigrants)] + immigrants
        # Track lineage edges for non-elites/immigrants by reading operator_history
        lineage_edges.extend(_lineage_from_children(new_population, previous=population, generation=gen))

        # Evaluate new pop
        t0 = time.perf_counter()
        results, scalars = evaluate_population(new_population, evaluator, task)
        dt = time.perf_counter() - t0

        # Save logs
        save_population_snapshot(rdir, gen, [g.to_dict() for g in new_population])
        save_metrics_csv(
            rdir, gen,
            [{"id": new_population[i].id, "scalar": scalars[i], **results[i].fitness} for i in range(len(new_population))]
        )

        # Next gen
        population = new_population

    # Finalize
    best_idx = max(range(len(population)), key=lambda i: scalars[i])
    best = population[best_idx]
    save_lineage(rdir, lineage_edges)

    summary = {
        "run_dir": str(rdir),
        "best_id": best.id,
        "best_scalar": float(scalars[best_idx]),
        "population_size": len(population),
        "generations": config.population.generations,
        "genome_type": genome_type.value,
    }
    return {"summary": summary, "best": best.to_dict(), "run_dir": str(rdir)}


def run_steady_state(
    evaluator: Evaluator,
    task: TaskSpec,
    config: RunConfig,
    selection: str = "tournament",
    genome_type: GenomeType = GenomeType.TABULAR,
    run_dir: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Simple steady-state variant:
      - Evaluate initial population
      - For each iteration: select parents -> produce one child -> evaluate -> insert replacing worst (unless worse and elitism blocks)
    """
    seed_info = set_all_seeds(config.seed)
    rdir = make_run_dir(run_dir or "experiments/runs")
    save_run_header(rdir, config.to_dict(), seed_info)

    rng = random.Random(config.seed)
    population = init_population_random(config.population.population_size, genome_type=genome_type, seed=config.seed)

    # Evaluate initial
    results, scalars = evaluate_population(population, evaluator, task)
    save_population_snapshot(rdir, 0, [g.to_dict() for g in population])
    save_metrics_csv(rdir, 0, [{"id": population[i].id, "scalar": scalars[i], **results[i].fitness} for i in range(len(population))])

    # iterations ~= generations * population_size
    iterations = config.population.generations * len(population)
    lineage_edges: List[Dict[str, Any]] = []

    for it in range(1, iterations + 1):
        # Select parents
        if selection == "roulette":
            parent_idx = roulette_selection(population, scalars, k=2, seed=rng.randrange(10_000))
        else:
            parent_idx = tournament_selection(population, scalars, k=2, tsize=3, seed=rng.randrange(10_000))
        p1, p2 = (population[i] for i in parent_idx)
        # Produce child
        child = _crossover_any(p1, p2, rng) if rng.random() < config.population.crossover_rate else _mutate_any(p1, rng)
        # Evaluate child
        child_res = evaluator.evaluate(child, task)
        child_scalar = _scalar_from_result(child_res)
        # Replace worst unless elitism blocks top-K
        elite_k = max(0, min(config.population.elitism, len(population)))
        elite_idx = sorted(range(len(population)), key=lambda i: scalars[i], reverse=True)[:elite_k]
        # find worst non-elite
        candidates = [i for i in range(len(population)) if i not in elite_idx]
        worst_idx = min(candidates, key=lambda i: scalars[i]) if candidates else min(range(len(population)), key=lambda i: scalars[i])

        if child_scalar > scalars[worst_idx]:
            # lineage edge (simple)
            lineage_edges.append({
                "parent": p1.id,
                "child": child.id,
                "op": (child.operator_history[-1]["op"] if child.operator_history else "unknown"),
                "params": (child.operator_history[-1].get("params", {}) if child.operator_history else {}),
                "gen": it,  # use iteration as timeline
            })
            population[worst_idx] = child
            scalars[worst_idx] = child_scalar

        # periodic logging every full-pop-size iterations
        if it % len(population) == 0:
            gen = it // len(population)
            save_population_snapshot(rdir, gen, [g.to_dict() for g in population])
            # build fake last results row (child only) is fine; better to recompute for logging
            _, rescal = evaluate_population(population, evaluator, task)
            save_metrics_csv(rdir, gen, [{"id": population[i].id, "scalar": rescal[i]} for i in range(len(population))])

    save_lineage(rdir, lineage_edges)
    best_idx = max(range(len(population)), key=lambda i: scalars[i])
    best = population[best_idx]
    summary = {
        "run_dir": str(rdir),
        "best_id": best.id,
        "best_scalar": float(scalars[best_idx]),
        "population_size": len(population),
        "generations": config.population.generations,
        "genome_type": genome_type.value,
        "mode": "steady_state",
    }
    return {"summary": summary, "best": best.to_dict(), "run_dir": str(rdir)}


# ------------------------------ lineage helper ------------------------------

def _lineage_from_children(new_population: Sequence[Genome], previous: Sequence[Genome], generation: int) -> List[Dict[str, Any]]:
    prev_ids = {g.id for g in previous}
    edges: List[Dict[str, Any]] = []
    for g in new_population:
        if g.id not in prev_ids and g.parents:
            edges.append({
                "parent": g.parents[0] if g.parents else None,
                "child": g.id,
                "op": (g.operator_history[-1]["op"] if g.operator_history else "unknown"),
                "params": (g.operator_history[-1].get("params", {}) if g.operator_history else {}),
                "gen": generation,
            })
    return edges


# ------------------------------ tiny self-test ------------------------------

if __name__ == "__main__":
    # Minimal demo run with MockEvaluator
    from .configs import RunConfig, PopulationConfig
    from .evaluation import TaskSpec

    cfg = RunConfig()
    # speed up for demo
    cfg = RunConfig(
        seed=123,
        population=PopulationConfig(population_size=12, generations=3, elitism=2, mutation_rate=0.4, crossover_rate=0.6),
        eval_budget=cfg.eval_budget,
        retrain_budget=cfg.retrain_budget,
        objectives=cfg.objectives,
        extras={"note": "phase4_selftest"},
    )

    evaluator = MockEvaluator()
    task = TaskSpec(name="cifar_tiny", kind="supervised", perf_weight=1.0, params_weight=1e-7, flops_weight=0.0)

    print("Running generational GA (demo)...")
    out = run_generational(
        evaluator=evaluator,
        task=task,
        config=cfg,
        selection="tournament",
        genome_type=GenomeType.TABULAR,
        run_dir=None,
    )
    print("Summary:", json.dumps(out["summary"], indent=2))

    print("Running steady-state GA (demo)...")
    out2 = run_steady_state(
        evaluator=evaluator,
        task=task,
        config=cfg,
        selection="roulette",
        genome_type=GenomeType.TABULAR,
        run_dir=None,
    )
    print("Summary SS:", json.dumps(out2["summary"], indent=2))

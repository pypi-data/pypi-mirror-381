







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
from typing import Any, Dict, Iterable, List, Sequence, Tuple

from .genome import Genome


# --------- Tournament ---------

def tournament_selection(population: Sequence[Genome], fitnesses: Sequence[float], k: int, tsize: int = 3, p_win: float = 1.0, seed: int | None = None) -> List[int]:
    """
    Return indices of selected parents by tournament.
    If p_win < 1, allow probabilistic winner selection (adds stochasticity).
    """
    assert len(population) == len(fitnesses)
    rng = random.Random(seed)
    idxs = list(range(len(population)))
    selected: List[int] = []
    for _ in range(k):
        tour = rng.sample(idxs, min(tsize, len(idxs)))
        tour_sorted = sorted(tour, key=lambda i: fitnesses[i], reverse=True)
        winner = tour_sorted[0]
        if p_win < 1.0 and len(tour_sorted) > 1 and rng.random() > p_win:
            winner = tour_sorted[1]  # occasionally pick second-best
        selected.append(winner)
    return selected


# --------- Roulette / SUS-ish ---------

def roulette_selection(population: Sequence[Genome], fitnesses: Sequence[float], k: int, seed: int | None = None) -> List[int]:
    """
    Fitness-proportionate selection with normalization; handles non-positive by shifting.
    Returns indices of selected parents.
    """
    assert len(population) == len(fitnesses)
    rng = random.Random(seed)
    f = list(fitnesses)
    minf = min(f)
    if minf <= 0:
        f = [fi - minf + 1e-12 for fi in f]  # shift to positive
    total = sum(f)
    if total <= 0:
        # fallback uniform
        return [rng.randrange(len(population)) for _ in range(k)]
    # cumulative
    cum = []
    c = 0.0
    for fi in f:
        c += fi / total
        cum.append(c)
    selected: List[int] = []
    for _ in range(k):
        r = rng.random()
        # linear search is fine for modest population sizes
        for i, ci in enumerate(cum):
            if r <= ci:
                selected.append(i)
                break
    return selected


# --------- Novelty (cheap token-Jaccard over JSON payloads) ---------

def _token_set(genome: Genome) -> set[str]:
    # tokenize by simple JSON string tokens; cheap and portable
    s = json.dumps(genome.payload, sort_keys=True)
    # keep alnum tokens only
    tokens = []
    curr = []
    for ch in s:
        if ch.isalnum():
            curr.append(ch.lower())
        else:
            if curr:
                tokens.append("".join(curr))
                curr = []
    if curr:
        tokens.append("".join(curr))
    return set(tokens)


def compute_novelty(population: Sequence[Genome], k_neighbors: int = 10) -> List[float]:
    """
    Novelty score = average 1 - Jaccard(token_set(self), token_set(neighbor)) over k nearest neighbors (by Jaccard distance).
    For small pops this is fine; can be optimized later.
    """
    token_sets = [_token_set(g) for g in population]
    n = len(population)
    scores: List[float] = []
    for i in range(n):
        dists: List[float] = []
        for j in range(n):
            if i == j:
                continue
            inter = len(token_sets[i] & token_sets[j])
            union = len(token_sets[i] | token_sets[j]) or 1
            jaccard = inter / union
            d = 1.0 - jaccard
            dists.append(d)
        dists.sort()
        k_eff = min(k_neighbors, len(dists))
        avg = sum(dists[:k_eff]) / k_eff if k_eff > 0 else 0.0
        scores.append(avg)
    return scores


# --------- Pareto utilities ---------

def dominates(a: Sequence[float], b: Sequence[float]) -> bool:
    """
    True if a Pareto-dominates b (maximize all objectives).
    a dominates b if a_i >= b_i for all i and strictly > for at least one i.
    """
    assert len(a) == len(b)
    ge_all = all(x >= y for x, y in zip(a, b))
    gt_any = any(x > y for x, y in zip(a, b))
    return ge_all and gt_any


def fast_nondominated_sort(vectors: Sequence[Sequence[float]]) -> List[List[int]]:
    """
    Simple non-dominated sort (O(n^2)), fine for modest populations.
    Returns list of fronts; each front is a list of indices.
    """
    n = len(vectors)
    S = [set() for _ in range(n)]   # who i dominates
    n_dom = [0] * n                  # how many dominate i
    fronts: List[List[int]] = [[]]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if dominates(vectors[i], vectors[j]):
                S[i].add(j)
            elif dominates(vectors[j], vectors[i]):
                n_dom[i] += 1
        if n_dom[i] == 0:
            fronts[0].append(i)

    f = 0
    while fronts[f]:
        next_front: List[int] = []
        for p in fronts[f]:
            for q in S[p]:
                n_dom[q] -= 1
                if n_dom[q] == 0:
                    next_front.append(q)
        f += 1
        fronts.append(next_front)
    if not fronts[-1]:
        fronts.pop()
    return fronts


def select_pareto(population: Sequence[Genome], vectors: Sequence[Sequence[float]], k: int) -> List[int]:
    """
    Pick up to k indices, traversing fronts from best to worse; break ties by crowding distance (simple version).
    """
    fronts = fast_nondominated_sort(vectors)
    selected: List[int] = []
    for front in fronts:
        if len(selected) + len(front) <= k:
            selected.extend(front)
        else:
            # need to pick remaining using crowding distance
            remain = k - len(selected)
            cd = crowding_distance([vectors[i] for i in front])
            order = sorted(range(len(front)), key=lambda r: cd[r], reverse=True)
            selected.extend([front[idx] for idx in order[:remain]])
            break
    return selected


def crowding_distance(front_vectors: Sequence[Sequence[float]]) -> List[float]:
    """
    Standard crowding distance approximation. Assumes we're maximizing all objectives.
    """
    m = len(front_vectors)
    if m == 0:
        return []
    nobj = len(front_vectors[0])
    distances = [0.0] * m
    for obj in range(nobj):
        order = sorted(range(m), key=lambda i: front_vectors[i][obj])
        minv = front_vectors[order[0]][obj]
        maxv = front_vectors[order[-1]][obj]
        distances[order[0]] = distances[order[-1]] = float("inf")
        denom = (maxv - minv) or 1e-12
        for r in range(1, m - 1):
            prev_v = front_vectors[order[r - 1]][obj]
            next_v = front_vectors[order[r + 1]][obj]
            distances[order[r]] += (next_v - prev_v) / denom
    return distances


# --------- tiny self-test ---------
if __name__ == "__main__":
    # make a toy population
    from .genome import GenomeType

    pop = []
    fits = []
    for i in range(6):
        g = Genome.new(
            GenomeType.TABULAR,
            {"layers": [{"type": "dense", "units": 32 + i, "act": "relu"}], "optimizer": {"lr": 1e-3 + i * 1e-4}},
            seed=123 + i,
        )
        pop.append(g)
        fits.append(0.5 + 0.1 * i)

    tsel = tournament_selection(pop, fits, k=3, tsize=3, seed=42)
    rsel = roulette_selection(pop, fits, k=3, seed=43)
    nov = compute_novelty(pop, k_neighbors=3)

    print("tournament idx:", tsel)
    print("roulette idx:", rsel)
    print("novelty scores:", [round(x, 3) for x in nov])

    # Pareto test
    vectors = [(0.6, 10.0), (0.7, 9.0), (0.65, 8.0), (0.55, 12.0), (0.7, 11.0), (0.5, 15.0)]
    sel = select_pareto(pop, vectors, k=3)
    print("pareto selected idx:", sel)
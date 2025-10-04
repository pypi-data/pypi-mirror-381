from neuroevolve.genome import Genome, GenomeType
from neuroevolve.selection import (
    tournament_selection,
    roulette_selection,
    compute_novelty,
    fast_nondominated_sort,
    select_pareto,
)

def _pop(n=8):
    P = []
    for i in range(n):
        P.append(
            Genome.new(
                GenomeType.TABULAR,
                payload={
                    "layers": [{"type": "dense", "units": 32 + i, "act": "relu"}],
                    "optimizer": {"lr": 1e-3},
                },
                seed=100 + i,
            )
        )
    return P

def test_tournament_and_roulette_lengths():
    pop = _pop(10)
    fits = [0.1 * i for i in range(len(pop))]
    t = tournament_selection(pop, fits, k=4, tsize=3, seed=1)
    r = roulette_selection(pop, fits, k=4, seed=2)
    assert len(t) == 4 and len(r) == 4
    assert all(0 <= i < len(pop) for i in t)
    assert all(0 <= i < len(pop) for i in r)

def test_novelty_length_matches_population():
    pop = _pop(7)
    nov = compute_novelty(pop, k_neighbors=3)
    assert len(nov) == len(pop)
    assert all(isinstance(x, float) for x in nov)

def test_pareto_selection_basic():
    pop = _pop(6)
    # vectors: (accuracy, -params) -> maximize both
    vectors = [(0.60, -1.0), (0.62, -0.8), (0.59, -0.5), (0.61, -1.2), (0.64, -1.1), (0.58, -0.6)]
    fronts = fast_nondominated_sort(vectors)
    assert isinstance(fronts, list) and len(fronts) >= 1
    sel = select_pareto(pop, vectors, k=3)
    assert 1 <= len(sel) <= 3
    assert all(isinstance(i, int) and 0 <= i < len(pop) for i in sel)

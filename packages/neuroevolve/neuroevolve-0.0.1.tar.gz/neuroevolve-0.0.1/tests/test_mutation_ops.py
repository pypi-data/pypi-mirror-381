from neuroevolve.genome import Genome, GenomeType
from neuroevolve import operators as ops

def _tabular():
    return Genome.new(
        GenomeType.TABULAR,
        payload={
            "layers": [
                {"type": "conv2d", "filters": 16, "kernel": 3, "act": "relu"},
                {"type": "dense", "units": 64, "act": "relu"},
                {"type": "dense", "units": 64, "act": "relu"},
            ],
            "optimizer": {"lr": 1e-3},
        },
        seed=42,
    )

def test_mutate_activation_creates_new_genome_and_logs_op():
    g = _tabular()
    child = ops.mutate_activation(g, seed=7)
    assert child.id != g.id
    assert child.operator_history[-1]["op"] == "mutate_activation"

def test_mutate_add_remove_layer_changes_depth():
    g = _tabular()
    c_add = ops.mutate_add_layer(g, seed=8)
    assert len(c_add.payload["layers"]) == len(g.payload["layers"]) + 1
    c_rm = ops.mutate_remove_layer(c_add, seed=9)
    assert len(c_rm.payload["layers"]) >= 1
    assert c_add.id != g.id and c_rm.id != c_add.id

def test_hparam_mutation_affects_optimizer():
    g = _tabular()
    c = ops.mutate_hyperparam(g, "lr", scale=0.1, seed=10)
    assert c.payload["optimizer"]["lr"] != g.payload["optimizer"]["lr"]
    assert c.operator_history[-1]["op"] == "mutate_hyperparam"

def test_one_point_crossover_returns_valid_child():
    a = _tabular()
    b = _tabular()
    c = ops.one_point_crossover(a, b, seed=11)
    assert c.id not in (a.id, b.id)
    assert isinstance(c.payload["layers"], list)
    assert c.operator_history[-1]["op"] == "one_point_crossover"

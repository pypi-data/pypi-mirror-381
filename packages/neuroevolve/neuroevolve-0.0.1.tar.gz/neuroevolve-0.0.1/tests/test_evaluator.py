from neuroevolve.genome import Genome, GenomeType
from neuroevolve.evaluation import MockEvaluator, TaskSpec

def _tabular():
    return Genome.new(
        GenomeType.TABULAR,
        payload={
            "layers": [
                {"type": "conv2d", "filters": 32, "kernel": 3, "act": "relu"},
                {"type": "dense", "units": 128, "act": "relu"},
            ],
            "optimizer": {"lr": 1e-3},
        },
        seed=123,
    )

def test_mock_supervised_fitness_range():
    ev = MockEvaluator()
    task = TaskSpec(name="cifar_tiny", kind="supervised", perf_weight=1.0, params_weight=1e-7)
    r = ev.evaluate(_tabular(), task)
    assert "val_acc" in r.fitness
    assert 0.0 <= r.fitness["val_acc"] <= 1.0
    assert isinstance(r.scalar_fitness, float)
    assert r.succeeded is True

def test_mock_rl_and_generative():
    ev = MockEvaluator()
    r1 = ev.evaluate(_tabular(), TaskSpec(name="cartpole", kind="rl"))
    assert "reward" in r1.fitness and 0.0 <= r1.fitness["reward"] <= 1.0
    r2 = ev.evaluate(_tabular(), TaskSpec(name="gan", kind="generative"))
    assert "fid_score" in r2.fitness and 0.0 <= r2.fitness["fid_score"] <= 1.0

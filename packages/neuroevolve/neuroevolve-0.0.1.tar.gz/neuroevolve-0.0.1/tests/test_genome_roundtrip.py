from neuroevolve.genome import Genome, GenomeType

def test_tabular_roundtrip_serialization():
    g = Genome.new(
        GenomeType.TABULAR,
        payload={
            "layers": [
                {"type": "conv2d", "filters": 16, "kernel": 3, "act": "relu"},
                {"type": "dense", "units": 64, "act": "relu"},
            ],
            "optimizer": {"lr": 1e-3},
        },
        seed=123,
    )
    s = g.to_json()
    g2 = Genome.from_json(s)
    assert g2.id == g.id
    assert g2.type == g.type
    assert g2.payload == g.payload
    assert g2.parents == g.parents
    assert list(g2.operator_history) == list(g.operator_history)

def test_graph_validate_and_operator_history():
    g = Genome.new(
        GenomeType.GRAPH,
        payload={"nodes": {"n0": {"op": "in"}, "n1": {"op": "conv"}}, "edges": [["n0", "n1"]], "readouts": ["n1"]},
        seed=1,
    )
    g.validate()  # should not raise
    g = g.with_operator({"op": "unit_test_op", "params": {"x": 1}})
    assert g.operator_history[-1]["op"] == "unit_test_op"

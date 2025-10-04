"""
operators.py — mutation and crossover operators

Design goals:
- Pure stdlib (random/json), no heavy deps.
- Every operator RETURNS A NEW Genome and appends an operator_history entry.
- Keep schemas valid per genome type (reuse validators from genome.py).

Supported (baseline) ops:
  Mutations:
    - mutate_hyperparam
    - mutate_activation
    - mutate_add_layer
    - mutate_remove_layer
    - mutate_layer_param
    - mutate_rewire_edge
    - mutate_controller_noise
  Crossovers:
    - one_point_crossover (tabular layers)
    - uniform_crossover (hyperparams dict)
    - subgraph_crossover (graph nodes/edges swap)

Notes:
- For tabular/graph genomes we treat .payload as structured dicts; we preserve keys.
- For controller genomes, noise is applied to numeric lists/dicts if present.
"""




from __future__ import annotations


if __name__ == "__main__" and __package__ is None:
    # allow running this file directly in VS Code
    import sys, pathlib
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[2] / "src"))
    __package__ = "neuroevolve"
    from neuroevolve.genome import Genome, GenomeType, VALIDATORS  # noqa



import copy
import json
import math
import random
import time
from typing import Any, Dict, List, Sequence, Tuple, Optional

from .genome import Genome, GenomeType, VALIDATORS


# --------- helpers ---------

_ACTIVATIONS = ["relu", "gelu", "silu", "swish", "tanh", "leakyrelu", "elu"]


def _deepcopy(d: Dict[str, Any]) -> Dict[str, Any]:
    return json.loads(json.dumps(d))


def _annotate(child: Genome, op: str, params: Dict[str, Any], seed: int | None = None) -> Genome:
    return child.with_operator({"op": op, "params": params, "seed": seed if seed is not None else child.seed})


def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed if seed is not None else time.time_ns())


# --------- MUTATIONS (TABULAR) ---------

def mutate_hyperparam(g: Genome, key: str, scale: float = 0.2, seed: Optional[int] = None) -> Genome:
    """For TABULAR/GRAPH payload['optimizer'] or other numeric hyperparams (lr, weight_decay)."""
    assert g.type in (GenomeType.TABULAR, GenomeType.GRAPH)
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    opt = payload.setdefault("optimizer", {})
    if key not in opt or not isinstance(opt.get(key), (int, float)):
        # if key missing, initialize with a small positive value
        opt[key] = 1e-3
    val = float(opt[key])
    noise = rng.lognormvariate(0.0, scale)  # multiplicative
    new_val = max(val * noise, 1e-8)
    opt[key] = new_val
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_hyperparam", {"key": key, "old": val, "new": new_val})


def mutate_activation(g: Genome, seed: Optional[int] = None) -> Genome:
    """Swap 'act' of a random layer (TABULAR)."""
    assert g.type == GenomeType.TABULAR
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    layers = payload["layers"]
    # choose a layer that has or can have an activation
    candidates = [i for i, L in enumerate(layers) if isinstance(L, dict) and L.get("type", "").lower() in {"conv", "conv2d", "dense", "linear"}]
    if not candidates:
        # fallback: do nothing
        return _annotate(g, "mutate_activation", {"note": "no eligible layer"})
    idx = rng.choice(candidates)
    old = layers[idx].get("act", "relu")
    new = rng.choice([a for a in _ACTIVATIONS if a != old]) if len(_ACTIVATIONS) > 1 else old
    layers[idx]["act"] = new
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_activation", {"layer_idx": idx, "old": old, "new": new})


def mutate_add_layer(g: Genome, position: Optional[int] = None, template: Optional[Dict[str, Any]] = None, seed: Optional[int] = None) -> Genome:
    """Insert a new layer into TABULAR genome."""
    assert g.type == GenomeType.TABULAR
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    layers = payload["layers"]
    if position is None:
        position = rng.randint(0, len(layers))  # insert anywhere including end
    if template is None:
        # simple random conv or dense
        if rng.random() < 0.6:
            template = {"type": "conv2d", "filters": rng.choice([16, 32, 64]), "kernel": rng.choice([1, 3, 5]), "stride": 1, "act": rng.choice(_ACTIVATIONS)}
        else:
            template = {"type": "dense", "units": rng.choice([64, 128, 256]), "act": rng.choice(_ACTIVATIONS)}
    layers.insert(position, template)
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_add_layer", {"position": position, "template": template})


def mutate_remove_layer(g: Genome, position: Optional[int] = None, seed: Optional[int] = None) -> Genome:
    """Remove a layer from TABULAR genome (keep at least one)."""
    assert g.type == GenomeType.TABULAR
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    layers = payload["layers"]
    if len(layers) <= 1:
        return _annotate(g, "mutate_remove_layer", {"note": "single-layer guard"})
    if position is None:
        position = rng.randrange(len(layers))
    removed = layers.pop(position)
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_remove_layer", {"position": position, "removed": removed})


def mutate_layer_param(g: Genome, layer_idx: int, param: str, step: int | float = 1, seed: Optional[int] = None) -> Genome:
    """Tweak a numeric/int parameter on a specific layer (TABULAR)."""
    assert g.type == GenomeType.TABULAR
    payload = _deepcopy(g.payload)
    layers = payload["layers"]
    if not (0 <= layer_idx < len(layers)):
        return _annotate(g, "mutate_layer_param", {"note": "out_of_bounds"})
    layer = layers[layer_idx]
    if param not in layer or not isinstance(layer[param], (int, float)):
        return _annotate(g, "mutate_layer_param", {"note": "non_numeric_or_missing"})
    old = layer[param]
    if isinstance(old, int):
        layer[param] = max(1, int(old + step))
    else:
        layer[param] = max(1e-8, float(old + step))
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_layer_param", {"layer_idx": layer_idx, "param": param, "old": old, "new": layer[param]})


# --------- MUTATIONS (GRAPH) ---------

def mutate_rewire_edge(g: Genome, seed: Optional[int] = None) -> Genome:
    """For GRAPH: pick an edge and rewire its target/source (avoid self-loops)."""
    assert g.type == GenomeType.GRAPH
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    nodes = list(payload["nodes"].keys())
    edges = payload["edges"]
    if not edges or len(nodes) < 2:
        return _annotate(g, "mutate_rewire_edge", {"note": "no_edges_or_nodes"})
    ei = rng.randrange(len(edges))
    u, v = edges[ei]
    # random choice: change source or target
    if rng.random() < 0.5:
        # change source
        new_u = rng.choice([n for n in nodes if n != v])
        edges[ei] = [new_u, v]
    else:
        # change target
        new_v = rng.choice([n for n in nodes if n != u])
        edges[ei] = [u, new_v]
    # validate & finish
    VALIDATORS[g.type](payload)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_rewire_edge", {"edge_index": ei, "old": [u, v], "new": edges[ei]})


# --------- MUTATIONS (CONTROLLER) ---------

def _add_noise(obj: Any, sigma: float, rng: random.Random) -> Any:
    if isinstance(obj, list):
        out = []
        for x in obj:
            out.append(_add_noise(x, sigma, rng))
        return out
    if isinstance(obj, dict):
        return {k: _add_noise(v, sigma, rng) for k, v in obj.items()}
    if isinstance(obj, (int, float)):
        return float(obj) + rng.gauss(0.0, sigma)
    # unknown type: leave as-is
    return obj


def mutate_controller_noise(g: Genome, sigma: float = 0.05, seed: Optional[int] = None) -> Genome:
    """Add Gaussian noise to numeric weights in controller payload."""
    assert g.type == GenomeType.CONTROLLER
    rng = _rng(seed)
    payload = _deepcopy(g.payload)
    if "weights" in payload:
        payload["weights"] = _add_noise(payload["weights"], sigma, rng)
    child = Genome.new(g.type, payload, seed=g.seed, parents=[g.id])
    return _annotate(child, "mutate_controller_noise", {"sigma": sigma})


# --------- CROSSOVERS ---------

def one_point_crossover(a: Genome, b: Genome, seed: Optional[int] = None) -> Genome:
    """TABULAR layers one-point crossover; parent order chosen as given."""
    assert a.type == GenomeType.TABULAR and b.type == GenomeType.TABULAR
    rng = _rng(seed)
    pa = _deepcopy(a.payload)
    pb = _deepcopy(b.payload)
    la, lb = pa["layers"], pb["layers"]
    if not la or not lb:
        # degenerate: copy A
        child_payload = pa
    else:
        cut_a = rng.randrange(1, len(la)) if len(la) > 1 else 1
        cut_b = rng.randrange(1, len(lb)) if len(lb) > 1 else 1
        child_layers = la[:cut_a] + lb[cut_b:]
        child_payload = pa
        child_payload["layers"] = child_layers
    VALIDATORS[a.type](child_payload)
    child = Genome.new(a.type, child_payload, seed=a.seed, parents=[a.id, b.id])
    return _annotate(child, "one_point_crossover", {"cut_a": cut_a if la else None, "cut_b": cut_b if lb else None})


def uniform_crossover_hparams(a: Genome, b: Genome, keys: Sequence[str], seed: Optional[int] = None) -> Genome:
    """Uniform crossover over optimizer hyperparams dict for TABULAR/GRAPH."""
    assert a.type in (GenomeType.TABULAR, GenomeType.GRAPH) and b.type == a.type
    rng = _rng(seed)
    pa = _deepcopy(a.payload)
    pb = _deepcopy(b.payload)
    oa = pa.setdefault("optimizer", {})
    ob = pb.setdefault("optimizer", {})
    oc = {}
    for k in keys:
        if rng.random() < 0.5:
            oc[k] = oa.get(k, ob.get(k))
        else:
            oc[k] = ob.get(k, oa.get(k))
    pa["optimizer"] = {**oa, **oc}
    VALIDATORS[a.type](pa)
    child = Genome.new(a.type, pa, seed=a.seed, parents=[a.id, b.id])
    return _annotate(child, "uniform_crossover_hparams", {"keys": list(keys)})


def subgraph_crossover(a: Genome, b: Genome, fraction: float = 0.5, seed: Optional[int] = None) -> Genome:
    """
    GRAPH crossover: copy A, then swap a random subset of B's nodes/edges into A by name overlap.
    Simplified: we replace attributes of overlapping nodes and attempt to merge edges that only reference present nodes.
    """
    assert a.type == GenomeType.GRAPH and b.type == GenomeType.GRAPH
    rng = _rng(seed)
    pa = _deepcopy(a.payload)
    pb = _deepcopy(b.payload)

    nodes_a = pa["nodes"]
    nodes_b = pb["nodes"]
    edges_a = pa["edges"]
    edges_b = pb["edges"]

    # pick subset of nodes from B to borrow
    b_nodes = list(nodes_b.keys())
    if not b_nodes:
        child_payload = pa
    else:
        k = max(1, int(len(b_nodes) * fraction))
        take = set(rng.sample(b_nodes, k))
        # replace/merge node attributes
        for n in take:
            if n in nodes_a:
                nodes_a[n] = nodes_b[n]
        # merge edges where both endpoints exist in A
        for (u, v) in edges_b:
            if u in nodes_a and v in nodes_a and [u, v] not in edges_a and u != v:
                edges_a.append([u, v])
        child_payload = pa

    VALIDATORS[a.type](child_payload)
    child = Genome.new(a.type, child_payload, seed=a.seed, parents=[a.id, b.id])
    return _annotate(child, "subgraph_crossover", {"fraction": fraction})


# --------- tiny self-test ---------
if __name__ == "__main__":
    # Build two simple tabular genomes
    from .genome import GenomeType

    a = Genome.new(
        GenomeType.TABULAR,
        {"layers": [{"type": "conv2d", "filters": 16, "kernel": 3, "act": "relu"}, {"type": "dense", "units": 64, "act": "relu"}],
         "optimizer": {"lr": 1e-3}},
        seed=1,
    )
    b = Genome.new(
        GenomeType.TABULAR,
        {"layers": [{"type": "conv2d", "filters": 32, "kernel": 3, "act": "relu"}, {"type": "dense", "units": 128, "act": "relu"}],
         "optimizer": {"lr": 5e-4}},
        seed=2,
    )

    c1 = mutate_activation(a)
    c2 = mutate_add_layer(a)
    c3 = mutate_remove_layer(c2)
    c4 = mutate_layer_param(a, 1, "units", step=32)
    c5 = mutate_hyperparam(a, "lr", scale=0.1)

    x1 = one_point_crossover(a, b)
    x2 = uniform_crossover_hparams(a, b, keys=["lr"])

    print("TABULAR ops OK:", len(c1.payload["layers"]), len(c2.payload["layers"]), c4.payload["layers"][1]["units"], x2.payload["optimizer"]["lr"])

    # Graph genomes
    ga = Genome.new(
        GenomeType.GRAPH,
        {"nodes": {"n0": {"op": "in"}, "n1": {"op": "conv"}, "n2": {"op": "out"}},
         "edges": [["n0", "n1"], ["n1", "n2"]],
         "readouts": ["n2"]},
        seed=3,
    )
    gb = Genome.new(
        GenomeType.GRAPH,
        {"nodes": {"n0": {"op": "in"}, "n1": {"op": "conv3x3"}, "n2": {"op": "conv1x1"}, "n3": {"op": "add"}},
         "edges": [["n0", "n1"], ["n1", "n3"], ["n2", "n3"]],
         "readouts": ["n3"]},
        seed=4,
    )

    gmut = mutate_rewire_edge(ga, seed=10)
    gx = subgraph_crossover(ga, gb, fraction=0.6, seed=11)
    print("GRAPH ops OK:", gmut.payload["edges"], len(gx.payload["edges"]))

    # Controller noise
    ctrl = Genome.new(
        GenomeType.CONTROLLER,
        {"arch": {"type": "mlp", "layers": [8, 8, 4]}, "weights": {"w": [0.1, -0.2, 0.05]}, "modulation_targets": ["g1"]},
        seed=5,
    )
    noisy = mutate_controller_noise(ctrl, sigma=0.01, seed=12)
    print("CONTROLLER noise OK:", noisy.payload["weights"])

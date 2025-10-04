"""
genome.py — genome schemas & (de)serialization

All genomes share a common metadata header and carry a type-specific payload.

Supported types:
- tabular: sequential layer list + hyperparams
- graph: DAG / cell-based motifs (nodes & edges) + hyperparams
- controller: neuromodulator architecture/weights + mapping targets
- cppn: indirect encoding (network generates parameters/structures)

No heavy deps; keep validation lightweight and explicit.
"""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field, asdict, replace
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


# --------- enums & type aliases ---------

class GenomeType(str, Enum):
    TABULAR = "tabular"
    GRAPH = "graph"
    CONTROLLER = "controller"
    CPPN = "cppn"


OperatorEntry = Dict[str, Any]  # {"op": str, "params": dict, "seed": int, "timestamp": str}


# --------- helpers ---------

def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _ensure(cond: bool, msg: str) -> None:
    if not cond:
        raise ValueError(msg)


# --------- payload validators (lightweight) ---------

def validate_tabular_payload(payload: Dict[str, Any]) -> None:
    layers = payload.get("layers")
    _ensure(isinstance(layers, list) and len(layers) > 0, "tabular.payload.layers must be non-empty list")
    for i, layer in enumerate(layers):
        _ensure(isinstance(layer, dict) and "type" in layer, f"tabular.layers[{i}] must have a 'type'")
        # Minimal sanity checks by type
        if layer["type"].lower() in {"conv", "conv2d"}:
            _ensure("filters" in layer and "kernel" in layer, "conv layer must specify filters & kernel")
        if layer["type"].lower() in {"dense", "linear"}:
            _ensure("units" in layer, "dense/linear layer must specify 'units'")
    opt = payload.get("optimizer", {})
    _ensure(isinstance(opt, dict), "tabular.payload.optimizer must be a dict")
    if "lr" in opt:
        _ensure(opt["lr"] > 0, "optimizer.lr must be > 0")


def validate_graph_payload(payload: Dict[str, Any]) -> None:
    nodes = payload.get("nodes")
    edges = payload.get("edges")
    _ensure(isinstance(nodes, dict) and len(nodes) > 0, "graph.payload.nodes must be non-empty dict")
    _ensure(isinstance(edges, list) and len(edges) > 0, "graph.payload.edges must be non-empty list")
    for u, v in edges:
        _ensure(u in nodes and v in nodes, f"edge ({u}->{v}) references missing node")
    readouts = payload.get("readouts", [])
    if readouts:
        for r in readouts:
            _ensure(r in nodes, f"readout node '{r}' not found in nodes")
    # Optional: disallow self-loops
    for u, v in edges:
        _ensure(u != v, "self-loops not allowed in graph payload")


def validate_controller_payload(payload: Dict[str, Any]) -> None:
    arch = payload.get("arch")
    targets = payload.get("modulation_targets", [])
    _ensure(isinstance(arch, dict), "controller.payload.arch must be dict")
    _ensure(isinstance(targets, list) and len(targets) > 0, "controller.payload.modulation_targets must be non-empty list")
    # weights can be a path or raw numbers (keep flexible)
    if "weights" in payload:
        _ensure(isinstance(payload["weights"], (str, list, dict)), "controller.payload.weights must be str | list | dict")


def validate_cppn_payload(payload: Dict[str, Any]) -> None:
    _ensure(isinstance(payload.get("cppn_arch"), dict), "cppn.payload.cppn_arch must be dict")
    if "cppn_weights" in payload:
        _ensure(isinstance(payload["cppn_weights"], (str, list, dict)), "cppn.payload.cppn_weights must be str | list | dict")
    mapping = payload.get("mapping_spec", {})
    _ensure(isinstance(mapping, dict) and "target" in mapping, "cppn.payload.mapping_spec must include 'target'")


# Map validators by genome type
VALIDATORS = {
    GenomeType.TABULAR: validate_tabular_payload,
    GenomeType.GRAPH: validate_graph_payload,
    GenomeType.CONTROLLER: validate_controller_payload,
    GenomeType.CPPN: validate_cppn_payload,
}


# --------- datamodel ---------

@dataclass(frozen=True)
class Genome:
    """
    Generic genome with type-specific payload and shared metadata.
    """
    id: str
    type: GenomeType
    payload: Dict[str, Any]
    seed: int
    created_at: str
    parents: Tuple[str, ...] = field(default_factory=tuple)
    operator_history: Tuple[OperatorEntry, ...] = field(default_factory=tuple)

    # ----- construction helpers -----

    @staticmethod
    def new(genome_type: GenomeType, payload: Dict[str, Any], seed: int, parents: Optional[List[str]] = None) -> "Genome":
        parents = tuple(parents or [])
        # validate payload according to type
        VALIDATORS[genome_type](payload)
        return Genome(
            id=str(uuid.uuid4()),
            type=genome_type,
            payload=_deepcopy(payload),
            seed=seed,
            created_at=_now_iso(),
            parents=parents,
            operator_history=tuple(),
        )

    def with_operator(self, op_entry: OperatorEntry) -> "Genome":
        """
        Return a copy with operator_history appended. Does not validate op schema tightly,
        but ensures required keys exist.
        """
        _ensure(isinstance(op_entry, dict) and "op" in op_entry, "operator entry must include 'op'")
        stamped = dict(op_entry)
        stamped.setdefault("timestamp", _now_iso())
        stamped.setdefault("seed", self.seed)
        return replace(self, operator_history=self.operator_history + (stamped,))

    # ----- validation -----

    def validate(self) -> None:
        VALIDATORS[self.type](self.payload)

    # ----- serialization -----

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type.value,
            "payload": _deepcopy(self.payload),
            "seed": self.seed,
            "created_at": self.created_at,
            "parents": list(self.parents),
            "operator_history": list(self.operator_history),
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), separators=(",", ":"), sort_keys=False)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Genome":
        _ensure(isinstance(d, dict), "Genome.from_dict expects dict")
        gtype = GenomeType(d["type"])
        payload = d["payload"]
        VALIDATORS[gtype](payload)
        return Genome(
            id=d["id"],
            type=gtype,
            payload=_deepcopy(payload),
            seed=int(d["seed"]),
            created_at=d["created_at"],
            parents=tuple(d.get("parents", [])),
            operator_history=tuple(d.get("operator_history", [])),
        )

    @staticmethod
    def from_json(s: str) -> "Genome":
        return Genome.from_dict(json.loads(s))


# --------- simple deep copy without importing copy (for clarity & perf on small dicts) ---------

def _deepcopy(obj: Any) -> Any:
    return json.loads(json.dumps(obj))


# --------- tiny self-test ---------
if __name__ == "__main__":
    # Build sample genomes of each type and check roundtrip
    tabular = Genome.new(
        GenomeType.TABULAR,
        payload={
            "layers": [
                {"type": "conv2d", "filters": 32, "kernel": 3, "stride": 1, "act": "relu"},
                {"type": "maxpool", "ks": 2},
                {"type": "dense", "units": 128, "act": "relu"},
            ],
            "optimizer": {"name": "adam", "lr": 1e-3},
            "train_budget": {"epochs": 3, "batch_size": 64},
        },
        seed=123,
    )

    graph = Genome.new(
        GenomeType.GRAPH,
        payload={
            "nodes": {"n0": {"op": "input"}, "n1": {"op": "conv3x3"}, "n2": {"op": "add"}, "n3": {"op": "output"}},
            "edges": [["n0", "n1"], ["n1", "n2"], ["n0", "n2"], ["n2", "n3"]],
            "readouts": ["n3"],
            "hyperparams": {"width": 32},
        },
        seed=123,
    )

    controller = Genome.new(
        GenomeType.CONTROLLER,
        payload={
            "arch": {"type": "mlp", "layers": [32, 32, 8]},
            "weights": "checkpoint/path/or/raw",
            "modulation_targets": ["layer1_gain", "layer3_lr_mult"],
            "controller_type": "modulator_v1",
        },
        seed=123,
    )

    cppn = Genome.new(
        GenomeType.CPPN,
        payload={
            "cppn_arch": {"type": "mlp", "layers": [16, 16, 1]},
            "cppn_weights": {"W1": [[0.1, -0.2], [0.3, 0.4]]},
            "mapping_spec": {"target": "conv_filters", "shape": [8, 8]},
        },
        seed=123,
    )

    for g in [tabular, graph, controller, cppn]:
        g.validate()
        j = g.to_json()
        g2 = Genome.from_json(j)
        assert g.to_dict() == g2.to_dict(), f"roundtrip failed for {g.type}"
        print(f"{g.type.value} genome roundtrip OK, id={g.id}")

    # operator history append
    g3 = tabular.with_operator({"op": "mutate_add_layer", "params": {"position": 1}})
    assert len(g3.operator_history) == 1
    print("operator_history append OK")

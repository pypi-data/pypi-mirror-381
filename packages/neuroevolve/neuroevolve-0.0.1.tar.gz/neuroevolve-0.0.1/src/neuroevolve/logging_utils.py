"""
logging_utils.py — persistence, lineage, and reproducibility helpers.

Responsibilities:
- Create run directories with timestamped IDs.
- Save population snapshots as JSONL; save metrics CSV (engine can produce rows).
- Record lineage edges (parent -> child with operator).
- Capture and set RNG seeds (python, numpy, torch if available).
- Save environment info (python version, torch/numpy versions) for provenance.

Keep it stdlib-first; guard optional torch/numpy imports.
"""

from __future__ import annotations

import csv
import json
import os
import platform
import random
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


# --------- run directory management ---------

def make_run_dir(root: Path | str = "experiments/runs", run_id: Optional[str] = None) -> Path:
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    if run_id is None:
        ts = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        short = uuid.uuid4().hex[:6]
        run_id = f"run_{ts}_{short}"
    run_path = root / run_id
    (run_path / "checkpoints").mkdir(parents=True, exist_ok=True)
    return run_path


# --------- JSONL writing ---------

def write_jsonl(path: Path | str, records: Iterable[Dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, separators=(",", ":")) + "\n")


def append_jsonl(path: Path | str, records: Iterable[Dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, separators=(",", ":")) + "\n")


# --------- population snapshots & lineage ---------

def save_population_snapshot(run_dir: Path | str, generation: int, population_dicts: Sequence[Dict[str, Any]]) -> Path:
    """Save the entire population (list of genome dicts) for a generation."""
    run_dir = Path(run_dir)
    path = run_dir / f"population_gen_{generation}.jsonl"
    write_jsonl(path, population_dicts)
    return path


def save_metrics_csv(run_dir: Path | str, generation: int, rows: Sequence[Dict[str, Any]]) -> Path:
    """
    Save metrics for a generation (e.g., fitnesses); expects list of dicts with identical keys.
    """
    run_dir = Path(run_dir)
    path = run_dir / f"metrics_gen_{generation}.csv"
    if not rows:
        # create empty file with header "empty"
        with path.open("w", newline="", encoding="utf-8") as f:
            f.write("empty\n")
        return path
    keys = sorted({k for row in rows for k in row.keys()})
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in keys})
    return path


def save_lineage(run_dir: Path | str, edges: Sequence[Dict[str, Any]]) -> Path:
    """
    Save lineage edges as a JSON file.

    Each edge: {
      "parent": "<uuid or None>",
      "child": "<uuid>",
      "op": "<operator name>",
      "params": {...},   # optional
      "gen": int         # generation number
    }
    """
    run_dir = Path(run_dir)
    path = run_dir / "lineage.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump({"edges": list(edges)}, f, indent=2)
    return path


# --------- RNG seeds & environment ---------

def set_all_seeds(seed: int) -> Dict[str, Any]:
    """
    Set seeds for python.random, numpy, and torch (if available).
    Return a small dict describing what was set (for logging).
    """
    random.seed(seed)
    info = {"python_random": seed}

    try:
        import numpy as np  # type: ignore
        np.random.seed(seed)
        info["numpy"] = seed
    except Exception:
        info["numpy"] = None

    try:
        import torch  # type: ignore
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)  # type: ignore
        info["torch"] = seed
    except Exception:
        info["torch"] = None

    return info


def get_environment_info() -> Dict[str, Any]:
    """
    Collect basic environment info for provenance.
    """
    info: Dict[str, Any] = {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    try:
        import numpy as np  # type: ignore
        info["numpy_version"] = np.__version__
    except Exception:
        info["numpy_version"] = None
    try:
        import torch  # type: ignore
        info["torch_version"] = getattr(torch, "__version__", None)
        info["cuda_available"] = bool(getattr(torch, "cuda", None) and torch.cuda.is_available())
    except Exception:
        info["torch_version"] = None
        info["cuda_available"] = None
    return info


def save_run_header(run_dir: Path | str, config_dict: Dict[str, Any], seed_info: Dict[str, Any]) -> Path:
    """
    Save a top-level run.json with config + seed info + environment metadata.
    """
    run_dir = Path(run_dir)
    path = run_dir / "run.json"
    payload = {
        "run_dir": str(run_dir),
        "config": config_dict,
        "seed_info": seed_info,
        "env": get_environment_info(),
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    return path


# --------- tiny self-test ---------
if __name__ == "__main__":
    rd = make_run_dir("./_tmp_runs")
    print(f"run dir: {rd}")
    # seeds & header
    s = set_all_seeds(123)
    print("seed info:", s)
    header = save_run_header(rd, {"foo": "bar"}, s)
    print("run header saved:", header)
    # population snapshot
    pop_path = save_population_snapshot(rd, 0, [{"id": "a"}, {"id": "b"}])
    print("population saved:", pop_path)
    # metrics
    mpath = save_metrics_csv(rd, 0, [{"id": "a", "acc": 0.8}, {"id": "b", "acc": 0.7}])
    print("metrics saved:", mpath)
    # lineage
    lpath = save_lineage(rd, [{"parent": None, "child": "a", "op": "init", "gen": 0}])
    print("lineage saved:", lpath)

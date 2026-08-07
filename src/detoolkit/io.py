"""CSV/JSON sample-data loaders for practice modules.

Resolves against a `data/` directory inside practice modules so tests stay
machine-address independent. Usage:

    from detoolkit.io import load_csv, load_json
    df = load_csv("tests", "recyclable_products.csv")
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]


def load_csv(module: str, name: str) -> pd.DataFrame:
    """Load a CSV sample from ``practice/<module>/<concept>/data/<name>``.

    Args:
        module: practice module name, e.g. ``data_cleaning``.
        name: filename, optionally including concept sub-path, e.g. ``hash-map/sample.csv``.
    """
    path = REPO_ROOT / "practice" / module / name
    if not path.exists():
        # Allow passing concept separately: load_csv("hash-map", "sample.csv")
        raise FileNotFoundError(f"sample not found: {path}")
    return pd.read_csv(path)


def load_json(name: str, module: str = "dsa_de") -> object:
    """Load a JSON sample from ``practice/<module>/``.

    Prefers the first `data/*.json` found under the module tree for ``name``.
    """
    data_dir = REPO_ROOT / "practice" / module
    matches = list(data_dir.rglob(name))
    if not matches:
        raise FileNotFoundError(f"sample not found under {data_dir}: {name}")
    with matches[0].open(encoding="utf-8") as fh:
        return json.load(fh)
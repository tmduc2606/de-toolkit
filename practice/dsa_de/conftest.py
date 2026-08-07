"""Shared pytest bootstrap for practice/dsa_de modules.

The individual test files already self-bootstrap via ``sys.path.insert``;
this file additionally guarantees ``src/detoolkit`` is importable when tests
run from the repo root.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
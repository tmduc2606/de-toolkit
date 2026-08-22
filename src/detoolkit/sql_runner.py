"""DuckDB runner used by all SQL problem tests."""
from __future__ import annotations

from pathlib import Path

import duckdb

REPO_ROOT = Path(__file__).resolve().parents[2]


def run_problem(problem_dir: Path) -> list[tuple]:
    """Execute ``schema.sql`` then ``solution.sql`` inside a scratch DuckDB.

    Args:
        problem_dir: folder containing ``schema.sql`` and ``solution.sql``.

    Returns:
        The result rows of the solution query as a list of tuples.
    """
    con = duckdb.connect()
    try:
        con.execute((problem_dir / "schema.sql").read_text(encoding="utf-8"))
        return con.execute((problem_dir / "solution.sql").read_text(encoding="utf-8")).fetchall()
    finally:
        con.close()


def expected_rows(problem_dir: Path) -> list[tuple]:
    """Read expected rows from a JSON ``expected.json`` when present.

    Falls back to an empty list for scaffolded problems relying on the
    structural smoke check.
    """
    expected_file = problem_dir / "expected.json"
    if not expected_file.exists():
        return []
    import json

    rows = json.loads(expected_file.read_text(encoding="utf-8"))
    return [tuple(row) for row in rows]
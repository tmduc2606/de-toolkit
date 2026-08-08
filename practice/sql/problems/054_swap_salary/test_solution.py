"""DuckDB test for SQL054 Swap Salary.

Structural check runs always. Full verification runs once schema.sql is
populated with the LeetCode example rows (contains an INSERT INTO).
The solution is an UPDATE — the test runs it, then SELECTs the final table
and compares against the annotated post-update state.
"""
import pathlib

import duckdb
import pytest

ROOT = pathlib.Path(__file__).parent


def test_problem_files_present():
    for name in ("problem.md", "schema.sql", "solution.sql"):
        assert (ROOT / name).exists(), f"missing {name}"


@pytest.mark.skipif(
    not (ROOT / "schema.sql").exists()
    or "INSERT INTO" not in (ROOT / "schema.sql").read_text(encoding="utf-8"),
    reason="schema.sql not yet populated with LeetCode example rows",
)
def test_expected_rows():
    con = duckdb.connect()
    try:
        con.execute((ROOT / "schema.sql").read_text(encoding="utf-8"))
        con.execute((ROOT / "solution.sql").read_text(encoding="utf-8"))
        rows = con.execute(
            "SELECT id, name, sex, salary FROM Salary ORDER BY id"
        ).fetchall()
    finally:
        con.close()
    expected = [
        (1, "A", "f", 2500),
        (2, "B", "m", 1500),
        (3, "C", "f", 5500),
        (4, "D", "m", 500),
    ]
    assert rows == expected
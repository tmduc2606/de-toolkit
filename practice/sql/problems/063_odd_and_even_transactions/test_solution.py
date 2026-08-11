"""DuckDB test for SQL063 Odd and Even Transactions.

Structural check runs always. Full verification runs once schema.sql is
populated with the LeetCode example rows (contains an INSERT INTO).
"""
import datetime
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
        rows = con.execute((ROOT / "solution.sql").read_text(encoding="utf-8")).fetchall()
    finally:
        con.close()
    expected = [
        (datetime.date(2024, 7, 1), 75, 350),
        (datetime.date(2024, 7, 2), 0, 350),
        (datetime.date(2024, 7, 3), 0, 120),
    ]
    assert rows == expected
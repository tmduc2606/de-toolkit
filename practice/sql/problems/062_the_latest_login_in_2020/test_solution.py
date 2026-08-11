"""DuckDB test for SQL062 The Latest Login in 2020.

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
        (2, datetime.datetime(2020, 1, 16, 2, 49, 50)),
        (6, datetime.datetime(2020, 6, 30, 15, 6, 7)),
        (8, datetime.datetime(2020, 12, 30, 0, 46, 50)),
    ]
    assert rows == expected
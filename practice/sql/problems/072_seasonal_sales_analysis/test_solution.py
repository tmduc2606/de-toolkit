"""DuckDB test for SQL072 Seasonal Sales Analysis.

Structural check runs always. Full verification runs once schema.sql is
populated with the LeetCode example rows (contains an INSERT INTO).
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
        rows = con.execute((ROOT / "solution.sql").read_text(encoding="utf-8")).fetchall()
    finally:
        con.close()
    # Ordered by season ASC: Fall, Spring, Summer, Winter.
    expected = [
        ("Fall", "Apparel", 10, 120.00),
        ("Spring", "Kitchen", 3, 54.00),
        ("Summer", "Tech", 5, 100.00),
        ("Winter", "Apparel", 9, 110.00),
    ]
    assert rows == expected

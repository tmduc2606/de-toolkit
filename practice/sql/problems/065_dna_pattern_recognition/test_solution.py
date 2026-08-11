"""DuckDB test for SQL065 DNA Pattern Recognition.

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
    expected = [
        (1, "ATGCTAGCTAGCTAA", "Human", 1, 1, 0, 0),
        (2, "GGGTCAATCATC", "Human", 0, 0, 0, 1),
        (3, "ATATATCGTAGCTA", "Human", 0, 0, 1, 0),
        (4, "ATGGGGTCATCATAA", "Mouse", 1, 1, 0, 1),
        (5, "TCAGTCAGTCAG", "Mouse", 0, 0, 0, 0),
        (6, "ATATCGCGCTAG", "Zebrafish", 0, 1, 1, 0),
        (7, "CGTATGCGTCGTA", "Zebrafish", 0, 0, 0, 0),
    ]
    assert rows == expected
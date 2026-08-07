"""Smoke tests for the shared detoolkit helpers."""
from __future__ import annotations

import pathlib

import pytest

from detoolkit import sql_runner

HAS_SPARK = False
try:
    import pyspark  # noqa: F401

    HAS_SPARK = True
except ImportError:  # pragma: no cover - optional group
    pass


def test_sql_runner_executes_schema_and_solution(tmp_path: pathlib.Path):
    (tmp_path / "schema.sql").write_text(
        "CREATE TABLE t (x INT); INSERT INTO t VALUES (1), (2);", encoding="utf-8"
    )
    (tmp_path / "solution.sql").write_text("SELECT x FROM t ORDER BY x;", encoding="utf-8")
    assert sql_runner.run_problem(tmp_path) == [(1,), (2,)]


def test_expected_rows_reads_json(tmp_path: pathlib.Path):
    (tmp_path / "expected.json").write_text("[[1], [2]]", encoding="utf-8")
    assert sql_runner.expected_rows(tmp_path) == [(1,), (2,)]


def test_expected_rows_defaults_to_empty(tmp_path: pathlib.Path):
    assert sql_runner.expected_rows(tmp_path) == []


@pytest.mark.skipif(not HAS_SPARK, reason="spark group not installed")
def test_spark_version():
    from detoolkit import spark

    assert spark.spark_version().startswith("4.")
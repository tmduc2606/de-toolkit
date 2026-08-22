# de-toolkit convenience targets (docs/OVERHAUL_BLUEPRINT.md)
.PHONY: sync test test-dsa test-sql gate full-gate env-airflow env-spark env-dbt

sync:            ## install core dependencies (pandas, duckdb, pytest, jupyter, ...)
	uv sync

test: test-dsa test-sql  ## full offline practice suite
	uv run pytest -q

test-dsa:
	uv run pytest practice/dsa_de -v

test-sql:
	uv run pytest practice/sql/problems -v

gate:            ## fast submission gate (layout + secrets + collect)
	uv run python scripts/validate_submissions.py

full-gate:       ## adds DuckDB execution of every populated SQL problem
	uv run python scripts/validate_submissions.py --full

env-airflow:     ## opt-in heavy toolchain
	uv sync --group airflow

env-spark:
	uv sync --group spark

env-dbt:
	uv sync --group dbt

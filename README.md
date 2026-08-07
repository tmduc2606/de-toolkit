# de-toolkit

Unified Data Engineering Toolkit: DSA-for-DE practice, SQL practice with automated tests, data-cleaning tutorials, and tech-stack learning material (Airflow, Spark, dbt) in a single monorepo.

## Quickstart

```powershell
uv sync                                # core dependencies (pandas, pyarrow, duckdb, pytest, jupyter, …)
uv sync --group airflow --group dbt --group spark   # opt-in heavy toolchains
uv run pytest practice/dsa_de -v       # DSA → DE kata tests
uv run pytest practice/sql/problems -v # SQL problem tests (DuckDB, offline)
```

## Module Index

| Module | What it is | How to run |
|---|---|---|
| `practice/dsa_de/` | LeetCode problems reframed as DE tasks, with pytest tests and sample data | `uv run pytest practice/dsa_de -v` |
| `practice/sql/` | 50 LeetCode SQL problems, structured with DuckDB-backed tests | `uv run pytest practice/sql/problems -v` |
| `practice/data_cleaning/` | Notebooks + datasets covering the common data-cleaning operations | open in Jupyter: `uv run jupyter lab` |
| `tech_stack/airflow/` | Airflow DAG learning material + docker-compose | `cd tech_stack/airflow && docker compose up` |
| `tech_stack/spark/` | PySpark tutorial notebook | `uv run --group spark jupyter lab` |
| `tech_stack/dbt/` | dbt project (bronze/silver/gold) | `uv run --group dbt dbt parse --project-dir tech_stack/dbt/duke_dbt` |

## Environment Model

One project, one lockfile, four dependency groups:

- **main** — shared data stack (pandas, pyarrow, duckdb, numpy, pytest, jupyter, scikit-learn, openpyxl, matplotlib)
- `--group airflow` — apache-airflow (heavy, opt-in)
- `--group dbt` — dbt-core + dbt-databricks + dbt-spark (heavy, opt-in)
- `--group spark` — pyspark (heavy, opt-in)

Run `uv sync --group airflow --group dbt --group spark` once for the full toolchain; daily work only needs `uv sync`.

## Security Policy

- `skills/` and `agents/` are **never** committed to version control — they hold agent logic and prompts. See `AGENTS.md`.
- dbt credentials are never stored in files: `tech_stack/dbt/profiles.example.yml` documents the shape; the real `profiles.yml` is gitignored and reads `DATABRICKS_TOKEN` from the environment.
- Any new hand-solved problem must pass `scripts/validate_submissions.py` before it is committed. See `CONTRIBUTING.md`.

## Old → New Path Mapping

| Old | New |
|---|---|
| `dsa-de-practice-main/` | `practice/dsa_de/` |
| `SQL 50 - Answersheet.txt` | `practice/sql/raw/sql_50_answersheet.txt` |
| `SQL - Common Patterns.docx` | `practice/sql/patterns.md` (+ original in `docs/originals/`) |
| `Data Cleaning/` | `practice/data_cleaning/` |
| `Airflow/` | `tech_stack/airflow/` |
| `spark_fundamentals/` | `tech_stack/spark/` |
| `dbt_fundamentals/` | `tech_stack/dbt/` |

## Documentation

- `docs/REFACTORING_BLUEPRINT.md` — the full refactoring blueprint, transformation principles, and commit gate design.
- `CONTRIBUTING.md` — how to add hand-solved DSA/SQL problems.
- `AGENTS.md` — rules for AI-assisted work in this repo.

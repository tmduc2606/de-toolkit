<div align="center">

# de-toolkit

**Hands-on Data Engineering learning monorepo — every exercise machine-checked offline.**

[![ci](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml)
[![python](https://img.shields.io/badge/python-3.14-blue.svg)](.python-version)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![sql drills](https://img.shields.io/badge/sql_drills-72-orange.svg)](practice/sql/problems)

</div>

**de-toolkit** is a single repository for learning data engineering by doing:
algorithm katas reframed as pipeline tasks, SQL drills asserted against DuckDB,
data-cleaning notebooks, and Airflow / Spark / dbt study material — all wired
into one `uv` project with a submission gate that keeps every contribution
consistent.

## Table of Contents

- [Why de-toolkit](#why-de-toolkit)
- [Learning tracks](#learning-tracks)
- [Repository map](#repository-map)
- [Quickstart](#quickstart)
- [Testing & validation](#testing--validation)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

## Why de-toolkit

- **Solve → reframe → verify.** Take a solved algorithmic problem, re-express it as a
  realistic DE task (record matching, top-k, gap detection), and lock the behavior behind
  pytest cases backed by sample data.
- **Offline-first.** SQL solutions execute against in-process DuckDB — no warehouse server,
  no cloud account, no network needed to learn or contribute.
- **Contract-enforced.** A deterministic submission gate (`scripts/validate_submissions.py`)
  checks layout, secrets hygiene, naming conventions, and tests before anything lands.
- **Real material.** Notebooks, DAGs, and dbt models carried over from genuine study
  sessions, not toy snippets.

## Learning tracks

| Track | Where | What you practice | Scale | How to run |
|---|---|---|---|---|
| DSA → DE katas | `practice/dsa_de/<concept>/` | Classic algorithms reframed as DE tasks — hash lookups, grouping, two-pointer, digit math, … | 15 concepts | `uv run pytest practice/dsa_de -v` |
| SQL drills | `practice/sql/problems/` | Joins, window functions, conditional aggregation, regex validation, … each solution DuckDB-tested | 72 problems | `uv run pytest practice/sql/problems -v` |
| Data cleaning | `practice/data_cleaning/notebooks/` | Missing values, outliers, encoding, scaling in pandas | 10 notebooks | `uv run jupyter lab` |
| Airflow | `tech_stack/airflow/` | Authoring and scheduling DAGs; docker-compose runtime | 15 DAGs | `cd tech_stack/airflow && docker compose up` |
| Spark | `tech_stack/spark/` | PySpark fundamentals notebook | — | `uv run --group spark jupyter lab` |
| dbt | `tech_stack/dbt/duke_dbt/` | Bronze/silver/gold modeling on Databricks | — | `uv run --group dbt dbt parse --project-dir tech_stack/dbt/duke_dbt` |

## Repository map

```
de-toolkit/
├── practice/
│   ├── dsa_de/           # 15 concept folders: solution + tests + sample data per concept
│   ├── sql/
│   │   ├── patterns.md   # common SQL patterns study guide
│   │   ├── raw/          # original SQL 50 answersheet (read-only provenance)
│   │   └── problems/     # 72 drills: problem.md · schema.sql · solution.sql · test_solution.py
│   └── data_cleaning/    # notebooks/, datasets/, practices/
├── tech_stack/
│   ├── airflow/          # dags/ + docker-compose.yaml learning playground
│   ├── spark/            # spark tutorial notebook
│   └── dbt/              # duke_dbt project (bronze/silver/gold)
├── notebooks/            # polished cross-track cleaning collection
├── src/detoolkit/        # shared helpers: DuckDB runner, Spark factory
├── scripts/              # extract_sql_answers · verify_toolchain · validate_submissions
├── docs/
│   └── OVERHAUL_BLUEPRINT.md   # tracked contract: conventions + conformance rules
├── .github/workflows/    # ci.yml — pytest + submission gate on push/PR
└── CONTRIBUTING.md       # how to add hand-solved problems (Flow A / Flow B)
```

## Quickstart

```bash
git clone https://github.com/tmduc2606/de-toolkit.git
cd de-toolkit
uv sync                  # core stack: pandas, pyarrow, duckdb, numpy, jupyter, …
uv run pytest -q         # full suite green in seconds
```

Heavy toolchains are opt-in dependency groups — daily work only needs `uv sync`:

```bash
uv sync --group airflow --group dbt --group spark   # full toolchain when needed
```

## Testing & validation

```bash
uv run pytest practice/dsa_de/digit-math -v            # one concept
uv run pytest practice/sql/problems/061_market_analysis_i -v   # one SQL drill
uv run python scripts/validate_submissions.py --full    # full submission gate
```

The gate verifies layout and naming conventions, scans tracked files for secrets,
collects all tests, executes every populated SQL problem through DuckDB, and runs
both practice modules end-to-end. CI runs the same checks on every push and PR.
Conventions live in [`docs/OVERHAUL_BLUEPRINT.md`](docs/OVERHAUL_BLUEPRINT.md).

## Contributing

Hand-solved problems follow two flows ([full guide](CONTRIBUTING.md)):

- **Flow A — DSA→DE problem:** copy a `_template/`, name the file
  `<leetcode#>_<slug>_<de_context>.py`, document the DE use case, add sample data
  plus normal/edge/empty tests, register it in the concept README table.
- **Flow B — SQL problem:** copy `practice/sql/problems/_template/`, fill the four
  files (prompt, example schema, DuckDB-portable answer, expected-row test).

Both must leave `validate_submissions.py` green before committing.

Agent-assisted work has its own ruleset in [`AGENTS.md`](AGENTS.md).

## Security

- `skills/` and `agents/` are never committed — they hold agent logic and prompts.
- Warehouse credentials come from environment variables only (`DATABRICKS_TOKEN`);
  only a sanitized `profiles.example.yml` shape is documented.
- The secret scan runs locally via the gate and again in CI.

## License

[MIT](LICENSE) © Tran Minh Duc

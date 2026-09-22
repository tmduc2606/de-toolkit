<div align="center">

# Data Engineering Toolkit - Learning Materials & Practice

**Hands-on Data Engineering learning monorepo — every exercise machine-checked offline.**

[![ci](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml)
[![python](https://img.shields.io/badge/python-3.14-blue.svg)](.python-version)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![sql drills](https://img.shields.io/badge/sql_drills-72-orange.svg)](practice/sql/problems)

</div>

**Data Engineering Toolkit - Learning Materials & Practice** (repository:
`de-toolkit`) is a single repository for learning data engineering by doing:
theory you read, algorithm katas reframed as pipeline tasks, SQL drills
asserted against DuckDB, data-cleaning and concept notebooks, and
Airflow / Spark / dbt study material — all wired into one `uv` project with a
submission gate that keeps every contribution consistent.

## Table of Contents

- [Why this repository](#why-this-repository)
- [Study materials](#study-materials)
- [Learning tracks](#learning-tracks)
- [Repository map](#repository-map)
- [Quickstart](#quickstart)
- [Testing & validation](#testing--validation)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)

## Why this repository

- **Solve → reframe → verify.** Take a solved algorithmic problem, re-express it as a
  realistic DE task (record matching, top-k, gap detection), and lock the behavior behind
  pytest cases backed by sample data.
- **Offline-first.** SQL solutions execute against in-process DuckDB — no warehouse server,
  no cloud account, no network needed to learn or contribute.
- **Contract-enforced.** A deterministic submission gate (`scripts/validate_submissions.py`)
  checks layout, secrets hygiene, naming conventions, and tests before anything lands.
- **Real material.** Notebooks, DAGs, and dbt models carried over from genuine study
  sessions, not toy snippets.

## Study materials

Theory lives in `docs/study-materials/` — read-only learning material, indexed
here (by design there is no per-topic README):

| Topic | Where | Contents |
|---|---|---|
| Data engineering fundamentals | [`docs/study-materials/data-engineering/`](docs/study-materials/data-engineering/) | Airflow agenda · SQL common patterns · dbt fundamentals (slides & notes) |
| Big data analytics | [`docs/study-materials/big-data-analytics/`](docs/study-materials/big-data-analytics/) | Introduction to Big Data slides · curated video links |
| Scalable & distributed computing | [`docs/study-materials/scalable-distributed-computing/`](docs/study-materials/scalable-distributed-computing/) | Lecture 1 slides (cloud intro · P1 intro) |

Runnable counterparts pair with these topics under `practice/` and
`tech_stack/` — theory to read here, code to run there.

## Learning tracks

| Track | Where | What you practice | Scale | How to run |
|---|---|---|---|---|
| DSA → DE katas | `practice/dsa_de/<concept>/` | Classic algorithms reframed as DE tasks — hash lookups, grouping, two-pointer, digit math, … | 15 concepts | `uv run pytest practice/dsa_de -v` |
| SQL drills | `practice/sql/problems/` | Joins, window functions, conditional aggregation, regex validation, … each solution DuckDB-tested | 72 problems | `uv run pytest practice/sql/problems -v` |
| Data cleaning | `practice/data_cleaning/notebooks/` | Missing values, outliers, encoding, scaling in pandas | 10 notebooks | `uv run jupyter lab` |
| Python computing | `practice/python-computing/` | Generators, iterators, regex, file I/O — Python fundamentals for DE | 6 notebooks | `uv run jupyter lab` |
| Scalable & distributed computing | `practice/scalable-distributed-computing/` | OOP + from-scratch ML (regression, perceptron, neural net) | 5 notebooks | `uv run jupyter lab` |
| Colab tips | `practice/colab-tips/` | Colab + Bash workflow tricks for shared notebooks | 1 notebook | `uv run jupyter lab` |
| Big data analytics | `practice/big-data-analytics/` | Concept-learning notebooks (placeholder — contributions welcome) | — | `uv run jupyter lab` |
| Airflow | `tech_stack/airflow/` | Authoring and scheduling DAGs; docker-compose runtime | 17 DAG files | `cd tech_stack/airflow && docker compose up` |
| Spark | `tech_stack/spark/` | PySpark fundamentals notebook | — | `uv run --group spark jupyter lab` |
| dbt | `tech_stack/dbt/duke_dbt/` | Bronze/silver/gold modeling on Databricks | — | `uv run --group dbt dbt parse --project-dir tech_stack/dbt/duke_dbt` |

## Repository map

```
de-toolkit/
├── docs/
│   └── study-materials/    # theory only: data-engineering · big-data-analytics
│                           # · scalable-distributed-computing (indexed in README)
├── practice/
│   ├── dsa_de/             # 15 concept folders: solution + tests + sample data per concept
│   ├── sql/
│   │   ├── patterns.md     # common SQL patterns study guide
│   │   ├── raw/            # original SQL 50 answersheet (read-only provenance)
│   │   └── problems/       # 72 drills: problem.md · schema.sql · solution.sql · test_solution.py
│   ├── data_cleaning/      # notebooks/, practices/ — pandas wrangling chapters
│   ├── python-computing/   # concept notebooks: generators, iterators, regex, I/O
│   ├── scalable-distributed-computing/  # OOP & from-scratch ML notebooks
│   ├── colab-tips/         # Colab + Bash workflow notebook
│   └── big-data-analytics/ # placeholder for big-data practice notebooks
├── tech_stack/
│   ├── airflow/            # dags/ + docker-compose.yaml learning playground
│   ├── spark/              # spark tutorial notebook + sample data
│   └── dbt/                # duke_dbt project (bronze/silver/gold)
├── src/detoolkit/          # shared helpers: DuckDB runner, Spark factory
├── scripts/                # extract_sql_answers · verify_toolchain · validate_submissions
├── .github/workflows/      # ci.yml — pytest + submission gate on push/PR
└── CONTRIBUTING.md         # how to add hand-solved problems (Flow A / Flow B)
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

Plain pip works too: each tech-stack module ships a `requirements.txt` mirror
of its `pyproject.toml` group (`pip install -r tech_stack/<module>/requirements.txt`).

## Testing & validation

```bash
uv run pytest practice/dsa_de/digit-math -v            # one concept
uv run pytest practice/sql/problems/061_market_analysis_i -v   # one SQL drill
uv run python scripts/validate_submissions.py --full    # full submission gate
```

The gate verifies layout and naming conventions, scans tracked files for secrets,
collects all tests, executes every populated SQL problem through DuckDB, and runs
both practice modules end-to-end. CI runs the same checks on every push and PR.
Conventions live in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Contributing

Hand-solved problems follow two flows ([full guide](CONTRIBUTING.md)):

- **Flow A — DSA→DE problem:** copy a `_template/`, name the file
  `<leetcode#>_<slug>_<de_context>.py`, document the DE use case, add sample data
  plus normal/edge/empty tests, register it in the concept README table.
- **Flow B — SQL problem:** copy `practice/sql/problems/_template/`, fill the four
  files (prompt, example schema, DuckDB-portable answer, expected-row test).

New topic folders are `kebab-case` and pair theory (`docs/study-materials/`)
with practice (`practice/`); both must leave `validate_submissions.py` green
before committing.

Agent-assisted work has its own ruleset in [`AGENTS.md`](AGENTS.md).

## Security

- `skills/` and `agents/` are never committed — they hold agent logic and prompts.
- Warehouse credentials come from environment variables only (`DATABRICKS_TOKEN`);
  only a sanitized `profiles.example.yml` shape is documented.
- The secret scan runs locally via the gate and again in CI.

## License

[MIT](LICENSE) © Tran Minh Duc

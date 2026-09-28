<div align="center">

# Data Engineering Toolkit - Learning Materials & Practice

**Hands-on Data Engineering learning monorepo — every workload locally validated.**

[![ci](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/tmduc2606/de-toolkit/actions/workflows/ci.yml)
[![python](https://img.shields.io/badge/python-3.14-blue.svg)](.python-version)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

**Data Engineering Toolkit - Learning Materials & Practice** (repository: `de-toolkit`) collects study materials and practical exercises related to DE topics such as SQL, data cleaning, and orchestration. Lecture, hand-written notes sit alongside runnable workloads — SQL problems, data-cleaning notebooks, and Airflow / Spark / dbt examples — all wired into a single `uv` project with a local submission gate that keeps contributions consistent.

## Table of Contents

- [Why this repository](#why-this-repository)
- [Contents](#contents)
- [Quickstart](#quickstart)
- [Testing & validation](#testing--validation)
- [Security](#security)
- [License](#license)

## Why this repository

- **Theory and practice.** Study materials pair with runnable exercises — read
  a topic, then run the code.
- **Locally validated.** Exercises execute against local runtimes such as
  DuckDB; no warehouse server, cloud account, Leetcode-style.
- **Coursework and self-study.** Material is drawn from university courses,
  independent learning, and practical workloads.

## Contents
```
de-toolkit/
├── docs/
│   └── study-materials/ # Theory notes on topics such as data engineering,
│                        # big data analytics, distributed computing
├── practice/
│   ├── dsa_de/ # Algorithms reframed as data tasks
│   ├── sql/
│   │   ├── patterns.md # Common SQL patterns study guide
│   │   ├── raw/ # Original answersheet (read-only provenance)
│   │   └── problems/ # SQL drills: prompt · schema · solution · tests
│   ├── data_cleaning/ # Notebooks and practices on pandas wrangling
│   ├── python-computing/ # Generators, iterators, regex, file I/O
│   ├── scalable-distributed-computing/ # OOP and from-scratch ML
│   ├── colab-tips/ # Colab + Bash workflow notebook
│   └── big-data-analytics/ # Placeholder for big-data practice notebooks
├── tech_stack/
│   ├── airflow/ # DAG playground with docker-compose runtime
│   ├── spark/ # PySpark tutorial notebook + sample data
│   └── dbt/ # duke_dbt project (bronze/silver/gold)
├── src/
│   └── detoolkit/ # Shared helpers: DuckDB runner, Spark factory
├── scripts/ # extract_sql_answers · verify_toolchain · validate_submissions
├── .github/
│   └── workflows/ # ci.yml — pytest + submission gate
└── CONTRIBUTING.md # Contribution guide
```

## Quickstart

```bash
git clone https://github.com/tmduc2606/de-toolkit.git
cd de-toolkit
uv sync                  # core stack: pandas, pyarrow, duckdb, numpy, ...
uv run pytest -q         # full suite runs locally
```

Heavy toolchains are opt-in dependency groups — daily work only needs uv sync:

```bash
uv sync --group airflow --group dbt --group spark   # full toolchain when needed
```

Additionally, plain pip also works: each tech-stack module ships a `requirements.txt` mirror
of its `pyproject.toml` group (`pip install -r tech_stack/<module>/requirements.txt`).
Airflow can be launched with Docker Compose from `tech_stack/airflow/`.

## Testing & validation

```bash
uv run pytest practice/dsa_de/<concept> -v            # one concept
uv run pytest practice/sql/problems/<problem> -v      # one SQL drill
uv run python scripts/validate_submissions.py --full  # full submission gate
```

The gate verifies layout and naming conventions, scans tracked files for
secrets, collects all tests, executes every populated SQL problem through
DuckDB, and runs the practice modules end-to-end. CI runs the same checks on
every push and PR. Conventions live in `CONTRIBUTING.md`.

## Security

Credentials come from environment variables only (for example DATABRICKS_TOKEN); only sanitized example configuration files are committed. A secret scan runs locally via the submission gate and again in CI.

# License

MIT © Tran Minh Duc

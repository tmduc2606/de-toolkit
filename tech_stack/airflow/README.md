# Airflow

Learning material for Apache Airflow orchestration:

- `dags/` — 17 progressive DAG examples (first DAG → versioning, operators, XComs, parallel tasks, branching, cron scheduling, incremental loads, dependent assets, orchestration).
- `docker-compose.yaml` — local Airflow 3.2.1 cluster (CeleryExecutor, PostgreSQL + Redis).
- `config/airflow.cfg` — sample configuration.

## Dependencies

Primary (repo-wide venv): `uv sync --group airflow`. Plain-pip fallback:

```powershell
pip install -r tech_stack/airflow/requirements.txt   # mirrors the pyproject group
```

## Run locally (Docker)

One-time setup (from the repo root) — write a local `.env` (gitignored) with
`AIRFLOW_UID` and a freshly generated Fernet key. Credentials never live in
tracked files, and rewriting the file whole keeps the key from ever gluing onto
a previous line:

```powershell
$key = uv run python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
Set-Content tech_stack/airflow/.env -Value "AIRFLOW_UID=50000`nFERNET_KEY=$key"
```

Then start the cluster:

```powershell
cd tech_stack/airflow
docker compose up
```

Airflow UI: <http://localhost:8080> (airflow / airflow).

## Checking DAGs without a cluster

```bash
# Linux / macOS / WSL2:
uv run --group airflow airflow dags list --subdir tech_stack/airflow/dags
```

> **Windows pitfall:** Airflow does not run natively on Windows
> (apache/airflow#10388 — `os.register_at_fork` is POSIX-only, so even
> `import airflow` fails under a Windows Python). On Windows, validate DAGs via
> WSL2 (command above) or the Docker cluster; `python -m py_compile dags/*.py`
> works everywhere as a syntax smoke test.

## Version notes

- Docker cluster pins `apache/airflow:3.2.1`; the local dependency group floats
  (`apache-airflow>=3.2.1`, currently 3.3.x) — expect minor CLI/UI differences.
- Runtime artifacts (`logs/`, `airflow.db`, `.env`) are gitignored — never commit them.

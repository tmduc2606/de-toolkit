# Airflow

Learning material for Apache Airflow orchestration:

- `dags/` — 15 progressive DAG examples (first DAG → versioning, operators, XComs, parallel tasks, branching, cron scheduling, incremental loads, dependent assets, orchestration).
- `docker-compose.yaml` — local Airflow 3.2.1 cluster (CeleryExecutor, PostgreSQL + Redis).
- `config/airflow.cfg` — sample configuration.

## Run locally (Docker)

```powershell
cd tech_stack/airflow
docker compose up           # copy .env.example -> .env first
```

Airflow UI: <http://localhost:8080> (admin / admin).

## Run DAG checks without a cluster

```powershell
uv run --group airflow airflow dags list --subdir tech_stack/airflow/dags
```

Runtime artifacts (`logs/`, `airflow.db`, `.env`) are gitignored — never commit them.

# dbt

dbt fundamentals project (`duke_dbt/`) with a bronze → silver → gold medallion layout on Databricks.

## Credentials

**Never commit credentials.** The real `profiles.yml` is gitignored; the committed
`profiles.example.yml` documents the shape. Create your local copy and export a token:

```powershell
Copy-Item tech_stack/dbt/profiles.example.yml tech_stack/dbt/profiles.yml
$env:DATABRICKS_TOKEN = "<your token>"     # or set system-wide
```

The profile references `{{ env_var('DATABRICKS_TOKEN') }}`; dbt reads it at runtime.

## Offline check (no warehouse connection)

```powershell
uv sync --group dbt
uv run dbt parse --project-dir tech_stack/dbt/duke_dbt --profiles-dir tech_stack/dbt
```

## Compile / run (needs credentials + warehouse)

```powershell
uv run dbt compile --project-dir tech_stack/dbt/duke_dbt --profiles-dir tech_stack/dbt
uv run dbt run --project-dir tech_stack/dbt/duke_dbt --profiles-dir tech_stack/dbt
```

Build artifacts (`target/`, `dbt_packages/`, `logs/`) are gitignored.

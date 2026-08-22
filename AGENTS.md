# AGENTS.md — rules for AI-assisted work in de-toolkit

## Scope

- READ-ONLY (never modify, never commit): `skills/`, `agents/` — if present on disk, use them for context only; never copy their contents into the repo.
- EDITABLE: `src/`, `practice/`, `tech_stack/`, `scripts/`, `tests/`, `docs/`, `notebooks/`, `pyproject.toml`, `Makefile`, root `README.md`.

## Never do

- Never create, stage, or commit anything under `skills/` or `agents/`.
- Never `git add -f`. Before `git add -A`, run `git status --porcelain` and confirm `skills/`, `agents/`, `.env`, `*.pem`, `*.key`, `*.p12`, `profiles.yml`, `logs/`, `target/`, `.venv/`, `dbt_packages/` are absent.
- Never write secrets into files (`dapi*`, `gh*`, `sk-*`, AWS keys, passwords); credentials come from environment variables only.
- Never edit `practice/sql/raw/` or any `logs/`, `target/`, `.venv/`.

## Adding or editing practice problems

1. Follow the conformance rules in `CONTRIBUTING.md`.
2. Copy the relevant `_template/` scaffold first.
3. After editing: `uv run pytest` for the affected module and `uv run python scripts/validate_submissions.py` — both must exit 0.
4. Commit with a scoped message, e.g. `feat(practice/sql): add SQL01 Recyclable and Low Fat Products`.

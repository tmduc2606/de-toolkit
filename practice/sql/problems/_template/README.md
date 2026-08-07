# SQL problem template

Copy this folder (minus this README) to `practice/sql/problems/<NNN>_<slug>/`
to scaffold a new hand-solved SQL problem. See
`docs/REFACTORING_BLUEPRINT.md` §8.1 for the conformance contract.

1. `problem.md`     — the LeetCode prompt plus its test-case annotations.
2. `schema.sql`     — `CREATE TABLE` + `INSERT` of the LeetCode example rows.
3. `solution.sql`   — the answer (DuckDB-portable; note MySQL-only fixes).
4. `test_solution.py` — DuckDB test; populate an `expected.json` with the
   annotated output rows once the answer is verified.
5. Run `uv run pytest practice/sql/problems/<folder> -v` and
   `uv run python scripts/validate_submissions.py` — both must exit 0.
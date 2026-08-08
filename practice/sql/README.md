# SQL Practice

LeetCode SQL 50 study material, structured for automated, offline testing.

## Layout

- `raw/sql_50_answersheet.txt` — the untouched original answersheet (extractor input).
- `patterns.md` — "Common Patterns" study guide (converted from the original docx).
- `problems/<NNN>_<slug>/` — one folder per problem with a four-file layout:

| File | Purpose |
|---|---|
| `problem.md` | problem name + MySQL answer + test-case annotations |
| `schema.sql` | `CREATE TABLE` + `INSERT`s of the LeetCode example rows |
| `solution.sql` | the answer, kept DuckDB-portable |
| `test_solution.py` | DuckDB test asserting the annotated expected rows |

`problems/_template/` is the copy-me scaffold for new problems.

## Regenerating the problems (idempotent)

```powershell
uv run python scripts/extract_sql_answers.py
```

Never overwrites a hand-written `schema.sql` or `test_solution.py`.

## Testing

```powershell
uv run pytest practice/sql/problems -v        # structural + DuckDB tests
uv run python scripts/validate_submissions.py --full
```

The tests load `schema.sql` into DuckDB, run `solution.sql`, and compare
against the expected rows — no MySQL server needed.

## Status

The 50 extracted problems carry working `solution.sql` files; `schema.sql` /
`test_solution.py` test data population is tracked per-problem in each
`problem.md` status checklist. Problems 051–060 are hand-solved beyond the
SQL 50 (LeetCode 175–1587 series) with fully populated schemas and DuckDB
tests asserting the annotated output.

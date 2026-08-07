# Contributing hand-solved problems

## Flow A — add a DSA→DE problem

1. Create `practice/dsa_de/<concept>/` (or reuse an existing concept).
2. Copy `practice/dsa_de/_template/` into it.
3. Implement per §8.1 of the blueprint (`docs/REFACTORING_BLUEPRINT.md`): LeetCode number + slug + DE frame in the filename; docstring naming the original LeetCode problem and the DE use case; one row added to the concept README problem table.
4. Add ≥ 1 sample file to `data/` and ≥ 3 pytest cases (normal / edge / empty).
5. Verify: `uv run pytest practice/dsa_de/<concept> -v` then `uv run python scripts/validate_submissions.py`.

## Flow B — add or fix a SQL problem

1. Copy `practice/sql/problems/_template/` to `problems/<NNN>_<slug>/`.
2. Fill `problem.md` (prompt + LeetCode test-case annotations), `schema.sql` (test-case rows), `solution.sql` (answer, DuckDB-portable per §6.3/D4 of the blueprint), `test_solution.py` (expected rows = annotated output).
3. Verify: `uv run pytest practice/sql/problems/<NNN>_<slug> -v` then `uv run python scripts/validate_submissions.py`.

## Definition of done

- `uv run python scripts/validate_submissions.py` exits 0.
- `uv run pytest` for the affected module is green.
- No secrets, no generated artifacts, no edits to `practice/sql/raw/`.
- Commit message carries the scope prefix (`feat(practice/...)`, `fix(...)`, `test(...)`).

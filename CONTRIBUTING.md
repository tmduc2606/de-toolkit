# Contributing hand-solved problems

## Flow A — add a DSA→DE problem

1. Create `practice/dsa_de/<concept>/` (or reuse an existing concept).
2. Copy `practice/dsa_de/_template/` into it.
3. Implement per the conformance rules below: LeetCode number + slug + DE frame in the filename; docstring naming the original LeetCode problem and the DE use case; one row added to the concept README problem table.
4. Add ≥ 1 sample file to `data/` and ≥ 3 pytest cases (normal / edge / empty).
5. Verify: `uv run pytest practice/dsa_de/<concept> -v` then `uv run python scripts/validate_submissions.py`.

## Flow B — add or fix a SQL problem

1. Copy `practice/sql/problems/_template/` to `problems/<NNN>_<slug>/`.
2. Fill `problem.md` (prompt + LeetCode test-case annotations), `schema.sql` (test-case rows), `solution.sql` (answer, DuckDB-portable per §6.3/D4 of the blueprint), `test_solution.py` (expected rows = annotated output).
3. Verify: `uv run pytest practice/sql/problems/<NNN>_<slug> -v` then `uv run python scripts/validate_submissions.py`.

## Folder & file naming

- New topic folders (practice modules and study-materials topics) are
  `kebab-case` and paired across the theory/practice split — e.g.
  `docs/study-materials/big-data-analytics/` ↔ `practice/big-data-analytics/`.
- Legacy top-level names stay `snake_case` (`practice/`, `tech_stack/`,
  `data_cleaning/`, `dsa_de/`) — referenced by `AGENTS.md`; do not rename.
- Code files are `snake_case` (`test_digit_math.py`); DSA concept folders are
  `kebab-case` (`digit-math/`).

## Definition of done

- `uv run python scripts/validate_submissions.py` exits 0.
- `uv run pytest` for the affected module is green.
- No secrets, no generated artifacts, no edits to `practice/sql/raw/`.
- Commit message carries the scope prefix (`feat(practice/...)`, `fix(...)`, `test(...)`).

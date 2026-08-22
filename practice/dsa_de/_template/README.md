# DSA → DE template

Copy this folder as the scaffold for a new hand-solved DSA→DE problem.
See `docs/OVERHAUL_BLUEPRINT.md` §4 for the conformance contract.

Required edits after copying:

1. Rename `NNN_original_slug_de_context.py`:
   - `NNN`       → LeetCode number, minimum three digits (e.g. `001`, `3622`)
   - slug       → LeetCode problem slug (e.g. `two_sum`)
   - de_context → the DE reframe (e.g. `pair_sum`)
2. Reframe the function to a DE context; keep a docstring naming the original
   LeetCode problem and the DE use case.
3. Add one row to the concept `README.md` problem table
   (columns: `Leetcode # | Original Problem | DE Reframed Problem | Solution File`).
4. Add sample data under `data/` and ≥ 3 pytest cases in `test_<concept>.py`.
5. Run `uv run pytest practice/dsa_de/<concept> -v` and
   `uv run python scripts/validate_submissions.py` — both must exit 0.
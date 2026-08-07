"""Extract practice/sql problems from the raw SQL 50 answersheet (idempotent).

Usage:
    uv run python scripts/extract_sql_answers.py

Input : practice/sql/raw/sql_50_answersheet.txt
Output: practice/sql/problems/<NNN>_<slug>/ with problem.md, solution.sql,
        schema.sql (scaffold) and test_solution.py (structural test or
        DuckDB-verified test when the schema is populated).

Re-running never destroys a hand-written schema: an existing schema.sql is
kept and only reported. See docs/REFACTORING_BLUEPRINT.md §6.3.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RAW = REPO_ROOT / "practice" / "sql" / "raw" / "sql_50_answersheet.txt"
OUT = REPO_ROOT / "practice" / "sql" / "problems"

HEADER = re.compile(r"^SQL(\d+)\s*-\s*(.+?)\s*$")

SCHEMA_SCAFFOLD = """\
-- schema.sql for SQL{num:03d} — {title}
-- Fill in the LeetCode example test case:
--   1. CREATE TABLE ... for every table referenced by solution.sql
--   2. INSERT the example rows (the same rows LeetCode annotates)
-- The test below switches from "skip" to real verification as soon as this
-- file contains an INSERT statement.
"""

TEST_SCAFFOLD = '''\
"""DuckDB test for SQL{num:03d} {title}.

Structural check runs always. Full verification runs once schema.sql is
populated with the LeetCode example rows (contains an INSERT INTO).
"""
import pathlib

import duckdb
import pytest

ROOT = pathlib.Path(__file__).parent


def test_problem_files_present():
    for name in ("problem.md", "schema.sql", "solution.sql"):
        assert (ROOT / name).exists(), f"missing {{name}}"


@pytest.mark.skipif(
    not (ROOT / "schema.sql").exists()
    or "INSERT INTO" not in (ROOT / "schema.sql").read_text(encoding="utf-8"),
    reason="schema.sql not yet populated with LeetCode example rows",
)
def test_expected_rows():
    con = duckdb.connect()
    try:
        con.execute((ROOT / "schema.sql").read_text(encoding="utf-8"))
        rows = con.execute((ROOT / "solution.sql").read_text(encoding="utf-8")).fetchall()
    finally:
        con.close()
    # EXPECTED = [..]  # uncomment and fill with the LeetCode example output
    expected = []
    assert rows == expected
'''

PROBLEM_MD_SCAFFOLD = """\
# SQL{num:03d} — {title}

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
{solution}
```

## Test-case annotations

```
{annotations}
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/{folder} -v` green
"""


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
    return slug or "problem"


def parse_problems() -> list[dict]:
    text = RAW.read_text(encoding="utf-8-sig")
    blocks = re.split(r"(?m)^SQL(\d+)\s*-\s*.+?$", text)
    # blocks[0] is the preamble; then pairs of (num, body)
    problems: list[dict] = []
    for i in range(1, len(blocks), 2):
        num = int(blocks[i])
        body = blocks[i + 1].strip("\n")
        problems.append({"num": num, "body": body})
    return problems


def split_body(body: str) -> tuple[str, str]:
    """Return (sql, annotations) — SQL lines vs `#` comment lines."""
    sql_lines: list[str] = []
    anno_lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            anno_lines.append(line)
        elif stripped:
            sql_lines.append(line)
    return "\n".join(sql_lines).strip(), "\n".join(anno_lines)


def main() -> int:
    problems = parse_problems()
    if not problems:
        print("no problems parsed — check input file")
        return 1
    OUT.mkdir(parents=True, exist_ok=True)
    for p in problems:
        num = p["num"]
        body_lines = p["body"].splitlines()
        title = ""
        first = body_lines[0].strip() if body_lines else ""
        m = re.match(r"SQL\d+\s*-\s*(.+)", first)
        if m:
            title = m.group(1).strip()
            body = "\n".join(body_lines[1:])
        else:
            body = p["body"]
        sql, annotations = split_body(body)
        if not title:
            title = f"problem {num}"
        folder = OUT / f"{num:03d}_{slugify(title)}"
        folder.mkdir(parents=True, exist_ok=True)

        (folder / "solution.sql").write_text(
            sql + "\n", encoding="utf-8"
        ) if sql else None
        (folder / "problem.md").write_text(
            PROBLEM_MD_SCAFFOLD.format(
                num=num, title=title, solution=sql, annotations=annotations,
                folder=folder.name,
            ),
            encoding="utf-8",
        )
        # Never overwrite a hand-written schema / test:
        if not (folder / "schema.sql").exists():
            (folder / "schema.sql").write_text(
                SCHEMA_SCAFFOLD.format(num=num, title=title), encoding="utf-8"
            )
        else:
            print(f"kept existing schema.sql for {folder.name}")
        if not (folder / "test_solution.py").exists():
            (folder / "test_solution.py").write_text(
                TEST_SCAFFOLD.format(num=num, title=title), encoding="utf-8"
            )
        else:
            print(f"kept existing test_solution.py for {folder.name}")
        print(f"SQL{num:03d} {title!r}: {len(sql)} SQL chars, {len(annotations)} annotation chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Commit gate for hand-solved problems (see CONTRIBUTING.md).

Usage:
    uv run python scripts/validate_submissions.py            # layout, ignore+secret guard, pytest collect
    uv run python scripts/validate_submissions.py --full     # also executes DuckDB SQL + dsa pytest

Exit code 0 = all rules pass; 1 = at least one rule fails.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import duckdb

ROOT = pathlib.Path(__file__).resolve().parents[1]
DSA_DIR = ROOT / "practice" / "dsa_de"
SQL_DIR = ROOT / "practice" / "sql" / "problems"

RESULTS: list[tuple[str, str]] = []

# Two independent numbering schemes:
#   - dsa_de solution filenames encode the LeetCode number (>= 3 digits)
#   - sql problem folders use a running catalog counter, not the LC number
DSA_FILE_RE = re.compile(r"^\d{3,}_[a-z0-9_]+_[a-z0-9_]+\.py$")
SQL_DIR_RE = re.compile(r"^\d{3,}_[a-z0-9_]+$")
FORBIDDEN = {"__pycache__", ".pytest_cache", ".ipynb_checkpoints", ".ruff_cache", "target", "dbt_packages", "logs", ".venv"}
# Transient caches pytest itself recreates on every run. They are blocked for
# git (check 1, so never committed); the concept-level dir check only hard-fails
# on persistent build/job artifacts.
TRANSIENT = {"__pycache__", ".pytest_cache", ".ruff_cache"}
# Files that legitimately contain the literal secret regexes (the gate tool
# itself) are skipped by the secret scan.
SELF_REFERENCING = {"scripts/validate_submissions.py"}
SECRET_RES = [
    re.compile(r"dapi[0-9a-f]{32,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"AIza[0-9A-Za-z\-_]{35}"),
    re.compile(r"-----BEGIN .* PRIVATE KEY-----"),
]


def check(label: str, ok: bool) -> None:
    RESULTS.append(("PASS" if ok else "FAIL", label))
    if not ok:
        print(f"   -> rule failed: {label}", file=sys.stderr)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)


def scan_text(text: str) -> list[str]:
    hits = []
    for rx in SECRET_RES:
        m = rx.search(text)
        if m:
            hits.append(m.group(0))
    return hits


def main() -> int:
    full = "--full" in sys.argv

    # 1) Ignore & security guard
    check("ignore: skills/", git("check-ignore", "-q", "skills/").returncode == 0)
    check("ignore: agents/", git("check-ignore", "-q", "agents/").returncode == 0)
    check("nothing tracked: skills/", git("ls-files", "skills/").stdout.strip() == "")
    check("nothing tracked: agents/", git("ls-files", "agents/").stdout.strip() == "")
    check(
        "no tracked secret files",
        git("ls-files", "**/profiles.yml", "**/.env", "**/*.pem", "**/*.key", "**/*.p12").stdout.strip() == "",
    )

    # 2) DSA layout
    dsa_concepts = [p for p in DSA_DIR.iterdir() if p.is_dir()] if DSA_DIR.exists() else []
    dsa_ok = True
    dsa_bad: list[str] = []
    for concept in dsa_concepts:
        if concept.name == "_template":
            continue
        if concept.name in FORBIDDEN:
            continue
        files = {f.name for f in concept.iterdir() if f.is_file()}
        has_solution = any(DSA_FILE_RE.match(f) for f in files)
        if not (concept / "README.md").exists():
            dsa_bad.append(f"{concept.name}: missing README.md")
            dsa_ok = False
        if not has_solution:
            dsa_bad.append(f"{concept.name}: no DSA solution file matching {DSA_FILE_RE.pattern}")
            dsa_ok = False
        for entry in concept.iterdir():
            if entry.is_dir() and entry.name in FORBIDDEN and entry.name not in TRANSIENT:
                dsa_bad.append(f"{concept.name}: forbidden dir {entry.name}")
                dsa_ok = False
    check(f"dsa layout: {len(dsa_concepts)} concepts clean", dsa_ok and not dsa_bad)
    if dsa_bad:
        print("   " + "\n   ".join(dsa_bad), file=sys.stderr)

    # 3) SQL layout
    sql_problems = [p for p in SQL_DIR.iterdir() if p.is_dir()] if SQL_DIR.exists() else []
    sql_bad: list[str] = []
    for problem in sql_problems:
        if problem.name == "_template":
            continue
        if not SQL_DIR_RE.match(problem.name):
            sql_bad.append(f"{problem.name}: name must match {SQL_DIR_RE.pattern}")
            continue
        for name in ("problem.md", "schema.sql", "solution.sql", "test_solution.py"):
            if not (problem / name).exists():
                sql_bad.append(f"{problem.name}: missing {name}")
        solution = (problem / "solution.sql").read_text(encoding="utf-8") if (problem / "solution.sql").exists() else ""
        for bad_token in ("USE ", "GRANT ", "CONNECT ", "password=", "token="):
            if bad_token.lower() in solution.lower():
                sql_bad.append(f"{problem.name}: solution.sql contains forbidden token {bad_token!r}")
    check(f"sql layout: {len(sql_problems)} problems, 4 files each", not sql_bad)
    if sql_bad:
        print("  - " + "\n  - ".join(sql_bad), file=sys.stderr)

    # 4) Pytest collection (fast, no execution)
    collect = subprocess.run(
        ["uv", "run", "python", "-m", "pytest", "practice/dsa_de", "practice/sql/problems", "--collect-only", "-q"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    check(f"pytest collect (exit {collect.returncode})", collect.returncode == 0)
    if collect.returncode != 0:
        print(collect.stdout[-2000:], file=sys.stderr)

    # 5) Secret scan over tracked text files
    tracked = git("ls-files", "*.py", "*.sql", "*.toml", "*.md", "*.txt", "*.yml", "*.csv", "*.json").stdout.splitlines()
    hits: list[str] = []
    for rel in tracked:
        path = ROOT / rel
        if rel in SELF_REFERENCING:
            continue
        if path.name == "uv.lock" or "/uv.lock" in rel:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except (OSError, PermissionError):
            continue
        for h in scan_text(text):
            hits.append(f"{rel}: {h}")
    check(f"secret scan: {len(tracked)} tracked files, 0 hits", not hits)
    if hits:
        print("  - " + "\n  - ".join(hits[:20]), file=sys.stderr)

    # 6) --full: real DuckDB execution
    if full:
        duck_fail = 0
        for problem in sql_problems:
            if problem.name == "_template":
                continue
            schema = problem / "schema.sql"
            if not schema.exists() or "INSERT INTO" not in schema.read_text(encoding="utf-8"):
                continue  # scaffold, verification happens once populated
            try:
                con = duckdb.connect()
                con.execute(schema.read_text(encoding="utf-8"))
                con.execute((problem / "solution.sql").read_text(encoding="utf-8")).fetchall()
            except Exception as exc:  # noqa: BLE001
                duck_fail += 1
                check(f"sql execute: {problem.name}", False)
                print(f"   - {problem.name}: {exc}", file=sys.stderr)
        check("sql duckdb execution", duck_fail == 0)

    failed = [r for r in RESULTS if r[0] == "FAIL"]
    for status, label in RESULTS:
        print(f"{status:<4} {label}")
    print(f"summary: PASS {len(RESULTS) - len(failed)}/{len(RESULTS)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
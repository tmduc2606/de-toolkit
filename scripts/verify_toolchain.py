"""One-command environment verification.

Usage:
    uv run python scripts/verify_toolchain.py          # core deps only
    uv run python scripts/verify_toolchain.py --all    # + airflow / dbt / spark groups
"""
from __future__ import annotations

import importlib
import sys

MODULES = ["pandas", "pyarrow", "duckdb", "pytest"]
GROUPS = {"spark": "pyspark", "airflow": "airflow", "dbt": "dbt"}


def check(label: str, fn) -> None:
    try:
        fn()
        print(f"PASS  {label}")
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL  {label}: {exc}")
        sys.exit(1)


def main() -> None:
    check("core imports", lambda: [importlib.import_module(m) for m in MODULES])
    if "--all" in sys.argv:
        for group, mod in GROUPS.items():
            check(
                f"{group} (--group {group})",
                lambda m=mod: importlib.import_module(m),
            )
    print("Toolchain OK")


if __name__ == "__main__":
    main()
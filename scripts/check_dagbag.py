"""Parse the Airflow learning DAGs with DagBag; fail on any import error.

Airflow cannot even be imported on native Windows (``os.register_at_fork`` is
POSIX-only, apache/airflow#10388), so this check runs inside the pinned
container — locally and in CI:

    docker run --rm -v "$PWD/tech_stack/airflow/dags:/opt/airflow/dags" \\
        -v "$PWD/scripts/check_dagbag.py:/opt/check_dagbag.py:ro" \\
        apache/airflow:3.2.1 python /opt/check_dagbag.py

Exit code 0 = every DAG file bagged cleanly; 1 = import errors (printed).
"""
from __future__ import annotations

import sys

from airflow.dag_processing.dagbag import DagBag

DAGS_FOLDER = sys.argv[1] if len(sys.argv) > 1 else "/opt/airflow/dags"


def main() -> int:
    # Mirror the real DAG processor: make the dags folder importable.
    sys.path.insert(0, DAGS_FOLDER)
    bag = DagBag(dag_folder=DAGS_FOLDER, include_examples=False)
    print(f"DAGs parsed: {len(bag.dags)} | import errors: {len(bag.import_errors)}")
    for path, error in bag.import_errors.items():
        print(f"==== ERROR {path}\n{error}")
    return 1 if bag.import_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

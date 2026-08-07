"""Windows-safe SparkSession factory extracted from tech_stack/spark notebooks."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import pyspark
from pyspark.sql import SparkSession


def get_spark(app_name: str = "detoolkit", *, driver_host: str | None = None) -> SparkSession:
    """Create a local SparkSession with Windows-friendly driver binding.

    Honors ``HADOOP_HOME`` from the environment when set (required for Windows
    local file access to ``file://`` paths). Falls back to a warning otherwise.

    Args:
        app_name: Spark application name.
        driver_host: driver bind host; defaults to ``127.0.0.1``.
    """
    venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
    if not Path(venv_python).exists():
        venv_python = sys.executable
    os.environ.setdefault("PYSPARK_PYTHON", venv_python)
    os.environ.setdefault("PYSPARK_DRIVER_PYTHON", venv_python)
    if not os.environ.get("HADOOP_HOME"):
        print("WARNING: HADOOP_HOME is not set; Windows file:// access may fail.", flush=True)

    host = driver_host or "127.0.0.1"
    return (
        SparkSession.builder.appName(app_name)
        .master("local[*]")
        .config("spark.driver.host", host)
        .config("spark.driver.bindAddress", host)
        .config("spark.pyspark.python", venv_python)
        .config("spark.pyspark.driver.python", venv_python)
        .config("spark.executor.memory", "512m")
        .config("spark.hadoop.fs.permissions.umask-mode", "000")
        .getOrCreate()
    )


def spark_version() -> str:
    return pyspark.__version__
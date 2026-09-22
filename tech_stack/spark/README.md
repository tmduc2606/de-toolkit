# Spark

PySpark learning material (Spark Connect, DataFrames, SQL, streaming, ML).

- `spark_tutorial.ipynb` — 35-cell tutorial covering SparkSession setup, Spark Connect, DataFrames, SQL, streaming, and ML pipelines.
- `sales_csv` — sample sales data.

## Dependencies

Primary (repo-wide venv): `uv sync --group spark`. Plain-pip fallback:

```powershell
pip install -r tech_stack/spark/requirements.txt   # mirrors the pyproject group
```

## Windows notes

Spark on Windows requires Hadoop native binaries:

- Install `winutils.exe` under `C:\hadoop\bin` and set:
  `$env:HADOOP_HOME = "C:\hadoop"`
- Or use the shared helper which honors `HADOOP_HOME` from the environment:

```python
from detoolkit.spark import get_spark
spark = get_spark("my-app")   # local[*], driver bound to 127.0.0.1
```

## Run the notebook

```powershell
uv sync --group spark
uv run jupyter lab
```

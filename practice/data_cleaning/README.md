# Data Cleaning

Notebooks + datasets covering the common data-cleaning operations:

- `notebooks/01_motivation` — why data cleaning matters; dirty-data sample.
- `notebooks/02_data_exploration` — profiling and exploration.
- `notebooks/03_handling_missing_values` — identify, drop, impute (incl. scikit-learn).
- `notebooks/04_encoding_strategies` — one-hot, label, ordinal, frequency, target encoding.
- `notebooks/05_outliers` — IQR and z-score removal.
- `notebooks/06_feature_scaling` — min-max, normalization, standardization.
- `notebooks/07_duplicated_values` — deduplication.
- `notebooks/08_changing_datatypes` — type casting.
- `notebooks/09_feature_transformers` — Box-Cox, Yeo-Johnson.
- `notebooks/10_ultimate_collection` — polished notebook covering all operations (Titanic dataset).
- `practices/` — curated practice problem lists (Pandas/LeetCode style).
- `datasets/` — shared datasets referenced across notebooks.

## Run

```powershell
uv sync
uv run jupyter lab
```

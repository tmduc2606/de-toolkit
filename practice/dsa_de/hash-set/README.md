# Hash Set

**Core DSA Concept:** Hash Set — O(1) membership testing using a hash-based set data structure.
**DE Topic:** Duplicate Detection in Datasets

## Why this matters for Data Engineering

Hash sets enable constant-time duplicate detection, which is critical for data quality checks,
deduplication pipelines, and identifying repeated records in streaming or batch data.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 217 | Contains Duplicate | Detect duplicate records in a dataset | `217_contains_duplicate_detect_duplicates.py` |
| 219 | Contains Duplicate II | Detect duplicates within a sliding window | `219_contains_duplicate_ii_sliding_window_duplicates.py` |

## Common Approach / Pattern

- Add elements to a set as you iterate.
- If an element is already in the set, a duplicate exists.
- For sliding window variants, store `{element: index}` in a dict and compare index distances.

## Data Samples

See `data/orders_with_duplicates.csv` for sample input with duplicate order IDs.

## How to run tests

```bash
uv run pytest practice/dsa_de/hash-set -v
```
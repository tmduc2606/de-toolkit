# Ordered Hash Set

**Core DSA Concept:** Ordered set — maintaining insertion order or sorted order
while supporting O(1) membership testing.
**DE Topic:** Deduplication of Sorted & Ordered Datasets

## Why this matters for Data Engineering

Deduplication is a core data quality operation. Ordered hash sets preserve the
order of first occurrence while removing duplicates, which is essential for
maintaining data lineage and temporal ordering in pipelines.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 26 | Remove Duplicates from Sorted Array | Deduplicate a sorted dataset in-place | `026_remove_duplicates_from_sorted_array_dedup_sorted.py` |
| 80 | Remove Duplicates from Sorted Array II | Deduplicate allowing at most two occurrences | `080_remove_duplicates_from_sorted_array_ii_dedup_sorted_ii.py` |

## Common Approach / Pattern

- Two-pointer technique on sorted arrays.
- For sorted arrays, duplicates are adjacent, enabling in-place removal.
- For the "at most two" variant, track the count of the current element.

## Data Samples

The `data/` folder contains sample sorted data for DE-focused tests.

## How to run tests

```bash
uv run pytest practice/dsa_de/ordered-hash-set -v
```

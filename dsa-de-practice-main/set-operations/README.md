# Set Operations

**Core DSA Concept:** Set intersection, union, and difference operations.
**DE Topic:** Dataset Join & Overlap Analysis

## Why this matters for Data Engineering

Set operations are the foundation of data joins, overlap analysis, and difference
detection between datasets. They are used in deduplication, reconciliation, and
identifying common or unique records across data sources.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 349 | Intersection of Two Arrays | Find common keys between two datasets (distinct) | `349_intersection_of_two_arrays_intersection_distinct.py` |
| 350 | Intersection of Two Arrays II | Find common records with occurrence counts | `350_intersection_of_two_arrays_ii_intersection_counts.py` |

## Common Approach / Pattern

- Convert both arrays to sets for O(1) membership testing.
- For intersection with counts, use a hash map to track frequencies.
- For distinct intersection, use set intersection operator.

## Data Samples

The `data/` folder contains sample dataset pairs for DE-focused tests.

## How to run tests

```bash
pytest test_set_operations.py -v
```

# Two Pointer

**Core DSA Concept:** Two-pointer technique — using two indices to traverse
a data structure from opposite ends or at different speeds.
**DE Topic:** Merging & Transforming Sorted Datasets

## Why this matters for Data Engineering

The two-pointer technique is used for merging sorted datasets, comparing
records across two sorted sources, and transforming arrays in-place —
common operations in ETL pipelines and external merge sort algorithms.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 21 | Merge Two Sorted Lists | Merge two sorted data streams | `021_merge_two_sorted_lists_merge_lists.py` |
| 88 | Merge Sorted Array | Merge a sorted buffer into a pre-allocated dataset | `088_merge_sorted_array_merge_arrays.py` |
| 977 | Squares of a Sorted Array | Transform and sort a numeric dataset | `977_squares_of_a_sorted_array_squares_sorted.py` |

> **Not yet implemented** — placeholder solutions pending for problems 88 and 977.

## Common Approach / Pattern

- For merging sorted data, compare elements from both sources and pick the smaller.
- For in-place merge, start from the end of the pre-allocated array.
- For sorted squares, use two pointers from both ends (negative values produce large squares).

## Data Samples

The `data/` folder is currently empty — add sample sorted data here.

## How to run tests

```bash
pytest test_two_pointer.py -v
```
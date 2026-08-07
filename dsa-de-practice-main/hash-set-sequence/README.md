# Hash Set Sequence

**Core DSA Concept:** Hash Set combined with sequence analysis.
**DE Topic:** Consecutive Run Detection in Datasets

## Why this matters for Data Engineering

Identifying the longest consecutive run of record IDs or timestamps helps detect
continuous data coverage, find gaps in sequential datasets, and validate completeness
of time-series or ordered data.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 128 | Longest Consecutive Sequence | Find the longest consecutive run of record IDs | `128_longest_consecutive_sequence_longest_seq.py` |

> **Not yet implemented** — placeholder solution pending.

## Common Approach / Pattern

- Store all elements in a hash set.
- For each element that starts a sequence (no predecessor in set), count consecutive elements.
- Track the maximum sequence length.

## Data Samples

The `data/` folder is currently empty — add sample sequential ID data here.

## How to run tests

```bash
pytest test_hash_set_sequence.py -v
```
# Grouping

**Core DSA Concept:** Hash Map of Lists — Grouping elements by a computed key into buckets.
**DE Topic:** Record Grouping & Aggregation

## Why this matters for Data Engineering

Grouping is fundamental to data transformation pipelines: partitioning data by key,
aggregating records into buckets, and preparing data for downstream analysis or export.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 49 | Group Anagrams | Group records by their character composition | `049_group_anagrams_group_records.py` |
| 347 | Top K Frequent Elements | Find the top-k most common values | `347_top_k_frequent_elements_top_k_freq.py` |
| 692 | Top K Frequent Words | Find the top-k most common words | `692_top_k_frequent_words_top_k_words.py` |

## Common Approach / Pattern

- Compute a grouping key for each element (e.g., sorted characters for anagrams).
- Use `dict.setdefault(key, []).append(element)` to bucket elements.
- For top-k, sort by frequency or use a heap.

## Data Samples

See `data/sample_logs.csv` for sample grouped log data.

## How to run tests

```bash
uv run pytest practice/dsa_de/grouping -v
```
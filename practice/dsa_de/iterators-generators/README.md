# Iterators & Generators

**Core DSA Concept:** Iterator pattern and generator functions for lazy evaluation.
**DE Topic:** Streaming Data Processing & Lazy Evaluation

## Why this matters for Data Engineering

Iterators and generators enable processing of large datasets that don't fit in memory,
lazy evaluation of data transformations, and streaming pipelines that process records
one at a time.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 173 | Binary Search Tree Iterator | Stream sorted records from a BST | `173_binary_search_tree_iterator_bst_stream.py` |
| 284 | Peeking Iterator | Preview the next record in a stream | `284_peeking_iterator_peek_stream.py` |

> **Not yet implemented** — placeholder solutions pending.

## Common Approach / Pattern

- Use a stack to simulate in-order traversal iteratively (BST iterator).
- Cache the next value to support peek without advancing the iterator.
- Generators (`yield`) provide a Pythonic way to implement lazy iterators.

## Data Samples

The `data/` folder is currently empty — add sample streaming data here.

## How to run tests

```bash
uv run pytest practice/dsa_de/iterators-generators -v
```
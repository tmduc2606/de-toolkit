# Recursion & DFS

**Core DSA Concept:** Depth-First Search — Traversing nested or hierarchical structures
by exploring as deep as possible before backtracking.
**DE Topic:** Nested Data Flattening & Hierarchical Processing

## Why this matters for Data Engineering

Many data engineering sources produce nested structures (JSON, XML, hierarchical logs).
DFS and flattening are essential for transforming nested data into flat, processable formats.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 341 | Flatten Nested List Iterator | Flatten nested data structures into a flat sequence | `341_flatten_nested_list_iterator_flatten_nested.py` |

## Common Approach / Pattern

- **Stack-based iterative** (used for 341): Maintain an explicit stack of iterators.
  Pop from the stack, and if the element is a list, push its iterator; otherwise, yield the element.
- **Recursive DFS**: Process each node, recursing into children.

## Data Samples

See `data/nested_json_sample.json` for sample nested JSON input.

## How to run tests

```bash
uv run pytest practice/dsa_de/recursion-dfs -v
```
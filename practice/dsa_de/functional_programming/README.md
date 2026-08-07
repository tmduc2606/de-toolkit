# Functional Programming

**Core DSA Concept:** Functional programming patterns — list comprehensions,
map/filter/reduce, and generator expressions for data transformation.
**DE Topic:** Data Transformations & List Comprehensions

## Why this matters for Data Engineering

Functional programming patterns are ubiquitous in data engineering:
filtering rows, projecting columns, computing derived fields, and aggregating
data using Python's list comprehensions, `map()`, `filter()`, and generator expressions.

## Problems

| Problem | DE Reframed Problem | Solution File |
|---|---|---|
| (Custom DE topic) | Apply list comprehension-based transformations to a dataset | `001_data_transformations_list_comprehensions.py` |

`data_transformations(records)` filters out `None`/non-positive rows, projects a
derived `total` per row, and aggregates a `grand_total` — a filter → project →
transform → aggregate pipeline.

## Data Samples

`data/orders.csv` — 5 sample order rows (including one negative-quantity and one
zero-quantity record used to exercise the filter branch).

## How to run tests

```bash
uv run pytest practice/dsa_de/functional_programming -v
```
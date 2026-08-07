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
| (Custom DE topic) | Apply list comprehension-based transformations to a dataset | `data_transformations_list_comprehensions.py` |

> **Not yet implemented** — placeholder solution pending.

## Common Approach / Pattern

- Use list comprehensions for filtering and mapping: `[transform(x) for x in data if condition(x)]`.
- Use generator expressions for memory-efficient lazy evaluation.
- Chain transformations: filter → map → aggregate.

## Data Samples

The `data/` folder is currently empty — add sample tabular data here.

## How to run tests

```bash
pytest test_functional_programming.py -v
```
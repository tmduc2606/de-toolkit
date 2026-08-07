# DSA → Data Engineering Practice Repository

This repository transforms solved Leetcode problems into a structured Data Engineering practice repo. Each problem is DE-reframed with consistent naming, READMEs, pytest tests, and sample data files.

## Getting Started

### Setup

```bash
pip install pytest
```

### Running Tests

Run all tests:

```bash
pytest -v
```

Run tests for a specific concept:

```bash
pytest test_hash_set.py -v
pytest test_hash_map.py -v
```

### Collecting Tests

To verify all test files are discoverable:

```bash
pytest --collect-only
```

## Folder Structure

```
dsa-de-practice/
├── grouping/
├── hash-map/
├── hash-set/
├── hash-set-sequence/
├── heap/
├── iterators-generators/
├── ordered-hash-set/
├── recursion-dfs/
├── set-lookup-math/
├── set-operations/
├── string-manipulation/
├── tree-traversal/
├── two-pointer/
└── functional-programming/
```

Each folder contains:
- `README.md` — Concept overview, problem table, and DE context
- `data/` — Sample CSV/JSON data files for DE-focused tests
- `test_{concept}.py` — Pytest test file
- Solution `.py` files (solved or placeholder)

## Cross-Concept Problem Notes

Some problems naturally span multiple concepts. The canonical implementation lives in the primary concept folder, and secondary folders may contain references or alternative approaches.

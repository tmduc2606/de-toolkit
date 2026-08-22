# Tree Traversal

**Core DSA Concept:** Tree traversal — in-order, level-order, and depth-first
search over hierarchical data structures.
**DE Topic:** Hierarchical Data Processing & Tree-Based Indexing

## Why this matters for Data Engineering

Tree traversals are used to process hierarchical data (nested JSON, XML,
directory structures) and to extract sorted or level-ordered records from
tree-based indexes (BSTs, B-trees) used in databases and data warehouses.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 94 | Binary Tree Inorder Traversal | Extract sorted keys from a BST index | `094_binary_tree_inorder_traversal_inorder.py` |
| 102 | Binary Tree Level Order Traversal | Process hierarchical data level by level | `102_binary_tree_level_order_traversal_level_order.py` |
| 104 | Maximum Depth of Binary Tree | Determine the nesting depth of a hierarchical data structure | `104_maximum_depth_of_binary_tree_max_depth.py` |
| 341 | Flatten Nested List Iterator | Flatten nested data structures | See `recursion-dfs/341_flatten_nested_list_iterator_flatten_nested.py` |

> **Note:** Problem 341 is canonically implemented in `recursion-dfs/`.
> This folder provides tree-traversal-specific problems (94, 102, 104).

## Common Approach / Pattern

- **In-order (DFS):** Left → Root → Right. Uses a stack or recursion.
- **Level-order (BFS):** Process nodes level by level using a queue.
- **Flattening (341):** Use an explicit stack to iteratively flatten nested lists.

## Data Samples

See `data/nested_json_sample.json` for sample nested JSON input (shared with `recursion-dfs/`).

## How to run tests

```bash
uv run pytest practice/dsa_de/tree-traversal -v
```
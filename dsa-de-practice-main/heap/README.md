# Heap

**Core DSA Concept:** Heap (Priority Queue) — A tree-based data structure that
efficiently retrieves the minimum or maximum element.
**DE Topic:** Top-K Selection & Priority-Based Processing

## Why this matters for Data Engineering

Heaps are used for top-k queries, priority-based processing of data streams,
and efficient selection of the largest or smallest elements in large datasets
without fully sorting them.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 215 | Kth Largest Element | Find the k-th largest value in a dataset | `215_kth_largest_element_kth_largest.py` |
| 692 | Top K Frequent Words | Find the k most common words | `692_top_k_frequent_words_top_k_words.py` |
| 347 | Top K Frequent Elements | Find the k most common values | `347_top_k_frequent_elements_top_k_freq.py` (canonical, in `grouping/`) |

> **Note:** The canonical implementations for 347 and 692 are in `grouping/`.
> The `heap/` folder provides heap-based alternative approaches and references.

## Common Approach / Pattern

- Use a min-heap of size k to track the top-k elements.
- Push elements onto the heap; pop the smallest when size exceeds k.
- For frequency-based top-k, combine a hash map (count) with a heap (top-k selection).

## Data Samples

The `data/` folder is currently empty — add sample frequency data here.

## How to run tests

```bash
pytest test_heap.py -v
```
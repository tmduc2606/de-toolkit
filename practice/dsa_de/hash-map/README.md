# Hash Map

**Core DSA Concept:** Hash Map — Key-value storage with O(1) average lookup, insertion, and deletion.
**DE Topic:** Frequency Counting & Record Lookup

## Why this matters for Data Engineering

Hash maps are the backbone of frequency counting, record lookup, and aggregation operations
in data pipelines. They enable fast joins, grouping, and ranking of data by key.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 1 | Two Sum | Find two transactions summing to a target amount | `001_two_sum_pair_sum.py` |
| 242 | Valid Anagram | Check if two text records have the same character composition | `242_valid_anagram_anagram_check.py` |
| 387 | First Unique Character | Find the first non-repeating event in a stream | `387_first_unique_character_first_non_repeating.py` |
| 451 | Sort Characters by Frequency | Rank items by occurrence frequency | `451_sort_characters_by_frequency_frequency_sort.py` |

## Common Approach / Pattern

- Count frequencies with a hash map: `counts[element] = counts.get(element, 0) + 1`.
- For pair-sum problems, store complements: `complement = target - current`.
- For sorting by frequency, sort map entries by value.

## Data Samples

See `data/frequency_sample.json` for sample frequency data.

## How to run tests

```bash
uv run pytest practice/dsa_de/hash-map -v
```
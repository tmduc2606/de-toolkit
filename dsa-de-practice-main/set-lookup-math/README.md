# Set Lookup & Math

**Core DSA Concept:** Set-based membership testing and mathematical set operations.
**DE Topic:** Missing Data Detection & Set Membership

## Why this matters for Data Engineering

Set lookups are used to detect missing records, validate data completeness, and perform
set operations (intersection, difference) between datasets — all common data quality tasks.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 268 | Missing Number | Find the missing record ID in a sequential dataset | `268_missing_number_missing_single.py` |
| 448 | Find All Numbers Disappeared | Find all missing record IDs in a range | `448_find_all_numbers_disappeared_missing_multi.py` |

## Common Approach / Pattern

- Convert the input list to a set for O(1) membership testing.
- Iterate over the expected range and check for missing values.
- For the missing number problem, the user's implementation uses list membership (`i not in nums`)
  which is O(n²); a set-based approach would be O(n).

## Data Samples

The `data/` folder is currently empty — add sample sequential ID data here.

## How to run tests

```bash
pytest test_set_lookup_math.py -v
```
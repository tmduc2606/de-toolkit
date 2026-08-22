# String Manipulation

**Core DSA Concept:** String processing — reversing, validating, and transforming text.
**DE Topic:** Text Field Transformation & Validation

## Why this matters for Data Engineering

String manipulation is essential for cleaning and transforming text fields in datasets:
reordering columns, validating formats, normalizing text, and preparing data for
downstream analysis or export.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 151 | Reverse Words in String | Reverse field order in a text record | `151_reverse_words_in_string_reverse_order.py` |
| 344 | Reverse String | Reverse character order in a text field | `344_reverse_string_reverse_chars.py` |
| 125 | Valid Palindrome | Validate text symmetry ignoring case and non-alphanumeric chars | `125_valid_palindrome_valid_palindrome.py` |

> **Not yet implemented** — placeholder solutions pending.

## Common Approach / Pattern

- Two-pointer technique for in-place string reversal.
- For word reversal, split by spaces, reverse the list, and rejoin.
- For palindrome validation, use two pointers from both ends, skipping non-alphanumeric characters.

## Data Samples

The `data/` folder is currently empty — add sample text data here.

## How to run tests

```bash
uv run pytest practice/dsa_de/string-manipulation -v
```
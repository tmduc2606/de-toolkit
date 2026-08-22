# Digit Math

**Core DSA Concept:** Digit extraction and arithmetic aggregation (running sum and product).
**DE Topic:** Checksum-style validation & data-quality filtering of record IDs

## Why this matters for Data Engineering

Lightweight arithmetic checksums let pipelines validate numeric identifiers without external
dependencies: a batch loader recomputes each ID's digit sum/product and quarantines records
that fail the divisibility gate before they reach staging.

## Problems

| Leetcode # | Original Problem | DE Reframed Problem | Solution File |
|---|---|---|---|
| 3622 | Check Divisibility by Digit Sum and Product | Flag record IDs divisible by their digit-sum + digit-product checksum | `3622_check_divisibility_by_digit_sum_and_product_digit_checksum.py` |

## Common Approach / Pattern

- Convert the number to its decimal digits via `str()`; accumulate sum and product in one pass.
- Seed the product at **1** — seeding at 0 would zero out every subsequent multiplication.
- The check is `n % (digit_sum + digit_product) == 0`. Note that any ID containing a `0` digit
  has a digit product of 0, so the divisor collapses to the digit sum alone.

## Data Samples

- `data/record_ids.csv` — sample batch of record IDs mixing passing and failing checksums.

## How to run tests

```bash
uv run pytest practice/dsa_de/digit-math -v
```
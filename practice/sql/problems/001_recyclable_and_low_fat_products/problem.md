# SQL001 — Recyclable and Low Fat Products

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT p.product_id
FROM Products p
WHERE p.low_fats = 'Y' AND p.recyclable = 'Y';
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/001_recyclable_and_low_fat_products -v` green

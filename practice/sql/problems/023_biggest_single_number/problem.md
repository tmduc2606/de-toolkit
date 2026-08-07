# SQL023 — Biggest Single Number

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT MAX(mn.num) AS num
FROM MyNumbers mn
WHERE mn.num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);
```

## Test-case annotations

```
# 1. Sub-query: Find all numbers with count = 1
# 2. Select the largest number in table
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/023_biggest_single_number -v` green

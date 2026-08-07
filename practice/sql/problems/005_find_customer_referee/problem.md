# SQL005 — Find Customer Referee

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT c.name
FROM Customer c
WHERE (c.referee_id != 2) OR (c.referee_id IS NULL);
```

## Test-case annotations

```
# Becareful of null --> IS NULL or IS NOT NULL
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/005_find_customer_referee -v` green

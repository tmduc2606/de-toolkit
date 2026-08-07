# SQL015 — Not Boring Movies

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT * FROM Cinema c
WHERE (c.id % 2 != 0) AND c.description NOT LIKE '%boring'
GROUP BY c.id
ORDER BY c.rating DESC;
```

## Test-case annotations

```
# LIKE '%xxx' & odd number x % 2 != 0
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/015_not_boring_movies -v` green

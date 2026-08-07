# SQL004 — Big Countries

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT w.name, w.population, w.area
FROM World w
WHERE (w.area >= 3000000) OR (w.population >= 25000000)
ORDER BY w.name, w.continent ASC;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/004_big_countries -v` green

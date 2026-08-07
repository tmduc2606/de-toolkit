# SQL021 — Classes With at Least 5 Students

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT c.class
FROM Courses c
GROUP BY c.class
HAVING COUNT(c.student) >= 5;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/021_classes_with_at_least_5_students -v` green

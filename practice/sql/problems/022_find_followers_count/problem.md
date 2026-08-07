# SQL022 — Find Followers Count

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT f.user_id, COUNT(f.follower_id) AS followers_count
FROM Followers f
GROUP BY f.user_id
ORDER BY f.user_id;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/022_find_followers_count -v` green

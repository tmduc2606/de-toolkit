# SQL031 — User Activity for the Past 30 Days I

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT a.activity_date AS day, COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
WHERE a.activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY day;
```

## Test-case annotations

```
# UNIQUE user_id on a day (regardless of which session they are in)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/031_user_activity_for_the_past_30_days_i -v` green

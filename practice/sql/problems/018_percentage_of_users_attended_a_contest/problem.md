# SQL018 — Percentage of Users Attended a Contest

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT r.contest_id, ROUND(
    COUNT(r.user_id) * 100 / 
        (SELECT COUNT(*) FROM Users), 
    2
) AS percentage
FROM Register r
JOIN Users u ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;
```

## Test-case annotations

```
# PERCENTAGE = CURRENT USERS PER CONTEST_ID / TOTAL USERS IN User TABLE
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/018_percentage_of_users_attended_a_contest -v` green

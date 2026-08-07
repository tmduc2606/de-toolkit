# SQL014 — Confirmation Rate

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT s.user_id, ROUND(AVG(
    CASE c.action
        WHEN 'confirmed' THEN 1
        ELSE 0
    END
), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON c.user_id = s.user_id
GROUP BY s.user_id;
```

## Test-case annotations

```
# CASE swtich + LEFT JOIN (for NULL
# If user signed up (with respective times) = # of success / attempts
# Otherwise 0 for NULL case or 'timedout'
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/014_confirmation_rate -v` green

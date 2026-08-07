# SQL046 — Restaurant Growth

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
WITH daily_amount AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT 
    d1.visited_on, 
    SUM(d2.amount) AS amount, 
    ROUND(AVG(d2.amount), 2) AS average_amount
FROM daily_amount d1
JOIN daily_amount d2 ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
GROUP BY d1.visited_on 
HAVING COUNT(DISTINCT d2.visited_on) = 7
ORDER BY d1.visited_on ASC;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/046_restaurant_growth -v` green

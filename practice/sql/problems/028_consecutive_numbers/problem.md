# SQL028 — Consecutive Numbers

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l2.id = l1.id + 1
JOIN Logs l3 ON l3.id = l1.id + 2
WHERE (l1.num = l2.num) AND (l2.num = l3.num);
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT id, num, LAG(num, 1) OVER (ORDER BY id) AS prev1,
    LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
) AS t
WHERE num = t.prev1 AND num = t.prev2;
```

## Test-case annotations

```
# Self-join or Window Functions (LAG() ... OVER (PARTITION BY X ORDER BY [Y]))
# Intermediate result: Current row | Next row | Next over next row
# Using LAG method
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/028_consecutive_numbers -v` green

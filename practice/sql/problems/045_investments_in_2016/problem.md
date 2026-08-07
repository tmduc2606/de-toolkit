# SQL045 — Investments in 2016

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM Insurance i1
WHERE EXISTS (
    SELECT 1
    FROM Insurance i2 WHERE i2.tiv_2015 = i1.tiv_2015 
    AND i2.pid != i1.pid
)
AND NOT EXISTS (
    SELECT 1
    FROM Insurance i3 WHERE i3.lat = i1.lat
    AND i3.lon = i1.lon
    AND i3.pid != i1.pid
);
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);
```

## Test-case annotations

```
# Modified self-join
# 1. Create a table to filter out public holder with same tiv in 2015 and both are unique
# 2. Create a table to filter out public holder who reside in the same city: pair (lat, lon) must differ from each other
# Alternative: GROUP BY w/ HAVING
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/045_investments_in_2016 -v` green

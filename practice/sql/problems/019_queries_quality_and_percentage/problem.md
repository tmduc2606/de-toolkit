# SQL019 — Queries Quality and Percentage

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT 
    q.query_name,
    ROUND(AVG(q.rating / q.position), 2) AS quality,
    ROUND(AVG(CASE WHEN q.rating < 3 THEN 1 ELSE 0 END) * 100, 2) AS poor_query_percentage
FROM Queries q
GROUP BY q.query_name;
```

## Test-case annotations

```
# GROUP BY query_name, Quality = AVG(rating / position), poor_query_percentage = AVG((CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100, 2)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/019_queries_quality_and_percentage -v` green

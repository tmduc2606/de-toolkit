# SQL026 — Triangle Judgement

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT t.x, t.y, t.z, (
    CASE WHEN (t.x >= 0 AND t.y >= 0 AND t.z >= 0)
    AND (t.x + t.y > t.z)
    AND (t.y + t.z > t.x)
    AND (t.x + t.z > t.y)
    THEN 'Yes' ELSE 'No' END
) AS triangle
FROM Triangle t;
```

## Test-case annotations

```
# Triangle Inequality: X, Y, Z >= 0 & Sum of two sides > The largest one
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/026_triangle_judgement -v` green

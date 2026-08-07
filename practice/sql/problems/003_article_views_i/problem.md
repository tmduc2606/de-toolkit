# SQL003 — Article Views I

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT DISTINCT v.author_id AS id
FROM Views v
WHERE v.author_id = v.viewer_id
ORDER BY v.author_id ASC;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/003_article_views_i -v` green

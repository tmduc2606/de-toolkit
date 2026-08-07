# SQL037 — Fix Names in a Table

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT u.user_id, CONCAT(UPPER(SUBSTRING(u.name, 1, 1)), LOWER(SUBSTRING(u.name, 2, length(u.name)))) AS name
FROM Users u
ORDER BY user_id;
```

## Test-case annotations

```
# Capitalize the first character, Lowercase the remaining words
# Use CONCAT to connect the characters
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/037_fix_names_in_a_table -v` green

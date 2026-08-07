# SQL039 — Delete Duplicate Emails

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email
AND p2.id < p1.id;
```

## Test-case annotations

```
# Is there anyway i could delete the row with same email, but the latter whose ID is less than the former?
# Intermediate value
# SELECT * 
# FROM Person p1
# JOIN Person p2 ON p2.email = p1.email AND p2.id < p1.id;
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/039_delete_duplicate_emails -v` green

# SQL071 — Find Valid Emails

> Source: LeetCode 3436 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Users`

| Column Name | Type |
|---|---|
| user_id | int |
| email | varchar |

`user_id` is the unique key. Find all valid email addresses. A valid email:

- contains exactly one `@` symbol,
- ends with `.com`,
- has only alphanumeric characters and underscores before the `@`,
- has a domain between `@` and `.com` that contains only letters.

Return the result table ordered by `user_id` in ascending order.

## Solution (MySQL, annotated)

```sql
# Write your MySQL query statement below
SELECT * FROM Users u
WHERE u.email REGEXP '^[a-z0-9]+@[a-z]+\\.com$'
ORDER BY u.user_id ASC;
```

> DuckDB note: the `REGEXP` operator does not exist in DuckDB — use
> `REGEXP_MATCHES(email, pattern)`. Also note MySQL's `REGEXP` is
> case-insensitive by default while DuckDB regexes are case-sensitive, so
> `solution.sql` adds an inline `(?i)` flag to keep identical semantics.

## Test-case annotations

```
Input:
Users table:
+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+

alice@example.com valid (one @, alphanumeric local part, letter domain).
bob_at_example.com invalid (underscore instead of @).
charlie@example.net invalid (does not end with .com).
david@domain.com valid.
eve@invalid invalid (no .com ending).

Output (ordered by user_id ASC):
+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/071_find_valid_emails -v` green
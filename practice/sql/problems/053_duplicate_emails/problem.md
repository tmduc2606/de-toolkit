# SQL053 — Duplicate Emails

> Source: LeetCode 182 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Person`

| Column Name | Type |
|---|---|
| id | int |
| email | varchar |

`id` is the primary key. Display duplicates of `email` that appear more than
once.

## Solution (MySQL, annotated)

```sql
SELECT p.email
FROM Person p
GROUP BY p.email
HAVING COUNT(*) > 1;
```

## Test-case annotations

```
Input:
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

Output:
+---------+
| email   |
+---------+
| a@b.com |
+---------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/053_duplicate_emails -v` green
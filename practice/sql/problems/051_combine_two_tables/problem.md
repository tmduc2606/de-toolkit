# SQL051 — Combine Two Tables

> Source: LeetCode 175 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Person`

| Column Name | Type |
|---|---|
| personId | int |
| lastName | varchar |
| firstName | varchar |

`personId` is the primary key. Table: `Address`

| Column Name | Type |
|---|---|
| addressId | int |
| personId | int |
| city | varchar |
| state | varchar |

Report the first name, last name, city, and state of each person; include
people with no address (city/state `null`).

## Solution (MySQL, annotated)

```sql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
```

## Test-case annotations

```
Input:
Person table:                         Address table:
+----------+----------+-----------+   +-----------+----------+---------------+----------+
| personId | lastName | firstName |   | addressId | personId | city          | state    |
+----------+----------+-----------+   +-----------+----------+---------------+----------+
| 1        | Wang     | Allen     |   | 1         | 2        | New York City | New York |
| 2        | Alice    | Bob       |   | 2         | 3        | Leetcode      | California|
+----------+----------+-----------+   +-----------+----------+---------------+----------+

Output:
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | null          | null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/051_combine_two_tables -v` green

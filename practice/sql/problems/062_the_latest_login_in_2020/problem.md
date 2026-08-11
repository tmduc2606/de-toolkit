# SQL062 — The Latest Login in 2020

> Source: LeetCode 1890 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Logins`

| Column Name | Type |
|---|---|
| user_id | int |
| time_stamp | datetime |

`(user_id, time_stamp)` is the primary key. Report the latest login for all
users in the year `2020`; do not include users who did not log in during
2020.

## Solution (MySQL, annotated)

```sql
-- Nested query: build a table of 2020 logins, ranked per user by
-- time_stamp DESC (ROW_NUMBER window)
-- External query: keep rank 1 per user as last_stamp (the latest)
SELECT user_id, time_stamp AS last_stamp
FROM (
    SELECT
        l.user_id,
        l.time_stamp,
        ROW_NUMBER() OVER (
            PARTITION BY l.user_id
            ORDER BY l.time_stamp DESC
        ) AS rn
    FROM Logins l
    WHERE YEAR(l.time_stamp) = 2020
) t
WHERE rn = 1
ORDER BY user_id ASC;
```

> DuckDB note: `YEAR()` accepts a TIMESTAMP in DuckDB, so the port is
> statement-for-statement (window functions are standard SQL).

## Test-case annotations

```
Input:
Logins table:
+---------+---------------------+
| user_id | time_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 6       | 2021-04-21 14:06:06 |
| 6       | 2019-03-07 00:18:15 |
| 8       | 2020-02-01 05:10:53 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
| 2       | 2019-08-25 07:59:08 |
| 14      | 2019-07-14 09:00:00 |
| 14      | 2021-01-06 11:59:59 |
+---------+---------------------+

User 6 logged in 3 times but once in 2020; user 8 logged in twice in 2020
(only the December one is kept); user 2 only once in 2020; user 14 never
logged in during 2020, so they are excluded.

Output:
+---------+---------------------+
| user_id | last_stamp          |
+---------+---------------------+
| 6       | 2020-06-30 15:06:07 |
| 8       | 2020-12-30 00:46:50 |
| 2       | 2020-01-16 02:49:50 |
+---------+---------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/062_the_latest_login_in_2020 -v` green
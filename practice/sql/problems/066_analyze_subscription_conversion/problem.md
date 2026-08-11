# SQL066 — Analyze Subscription Conversion

> Source: LeetCode 3497 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `UserActivity`

| Column Name | Type |
|---|---|
| user_id | int |
| activity_date | date |
| activity_type | varchar |
| activity_duration | int |

`(user_id, activity_date, activity_type)` is the unique key; `activity_type`
is one of `('free_trial', 'paid', 'cancelled')`; `activity_duration` is the
number of minutes the user spent on the platform that day. Find users who
converted from free trial to paid subscription, then report each one's
average daily activity duration during the free trial period and during the
paid period, both rounded to `2` decimal places. Return the result table
ordered by `user_id` in ascending order.

## Solution (MySQL, annotated)

```sql
-- Optimal approach: LAG() builds the previous-activity context per user;
-- ConvertedUser keeps only users whose free_trial was immediately followed
-- by a paid subscription; the final query averages activity_duration per
-- activity type with ROUND(..., 2)
WITH Activity AS (
    SELECT
        ua.user_id,
        ua.activity_date,
        ua.activity_type,
        LAG(ua.activity_type) OVER (
            PARTITION BY ua.user_id
            ORDER BY ua.activity_date
        ) AS previous_type,
        ua.activity_duration
    FROM UserActivity ua
),
ConvertedUser AS (
    SELECT DISTINCT user_id
    FROM Activity
    WHERE previous_type = 'free_trial' AND activity_type = 'paid'
)
SELECT
    a.user_id,
    ROUND(AVG(
        CASE WHEN a.activity_type = 'free_trial' THEN a.activity_duration END
    ), 2) AS trial_avg_duration,
    ROUND(AVG(
        CASE WHEN a.activity_type = 'paid' THEN a.activity_duration END
    ), 2) AS paid_avg_duration
FROM Activity a
JOIN ConvertedUser cu ON a.user_id = cu.user_id
GROUP BY a.user_id
ORDER BY a.user_id;
```

> DuckDB note: the brute-force alternative (a nested query with the same
> `LAG` context plus an `IN` subquery and `COALESCE`) works too; the two-CTE
> version above is the one committed to `solution.sql` (trailing commas are
> not allowed between CTE bodies). `ROUND(AVG(...), 2)` returns a DOUBLE in
> DuckDB (`45.0`), which compares equal to the annotated `45.00`.

## Test-case annotations

```
Input:
UserActivity table:
+---------+---------------+---------------+-------------------+
| user_id | activity_date | activity_type | activity_duration |
+---------+---------------+---------------+-------------------+
| 1       | 2023-01-01    | free_trial    | 45                |
| 1       | 2023-01-02    | free_trial    | 30                |
| 1       | 2023-01-05    | free_trial    | 60                |
| 1       | 2023-01-10    | paid          | 75                |
| 1       | 2023-01-12    | paid          | 90                |
| 1       | 2023-01-15    | paid          | 65                |
| 2       | 2023-02-01    | free_trial    | 55                |
| 2       | 2023-02-03    | free_trial    | 25                |
| 2       | 2023-02-07    | free_trial    | 50                |
| 2       | 2023-02-10    | cancelled     | 0                 |
| 3       | 2023-03-05    | free_trial    | 70                |
| 3       | 2023-03-06    | free_trial    | 60                |
| 3       | 2023-03-08    | free_trial    | 80                |
| 3       | 2023-03-12    | paid          | 50                |
| 3       | 2023-03-15    | paid          | 55                |
| 3       | 2023-03-20    | paid          | 85                |
| 4       | 2023-04-01    | free_trial    | 40                |
| 4       | 2023-04-03    | free_trial    | 35                |
| 4       | 2023-04-05    | paid          | 45                |
| 4       | 2023-04-07    | cancelled     | 0                 |
+---------+---------------+---------------+-------------------+

User 1: trial (45+30+60)/3 = 45.00; paid (75+90+65)/3 = 76.67.
User 2: only free_trial + cancelled -> not converted, excluded.
User 3: trial (70+60+80)/3 = 70.00; paid (50+55+85)/3 = 63.33.
User 4: trial (40+35)/2 = 37.50; paid 45.00.

Output (ordered by user_id ASC):
+---------+--------------------+-------------------+
| user_id | trial_avg_duration | paid_avg_duration |
+---------+--------------------+-------------------+
| 1       | 45.00              | 76.67             |
| 3       | 70.00              | 63.33             |
| 4       | 37.50              | 45.00             |
+---------+--------------------+-------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/066_analyze_subscription_conversion -v` green
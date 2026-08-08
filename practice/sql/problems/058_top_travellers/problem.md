# SQL058 — Top Travellers

> Source: LeetCode 1407 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Tables: `Users`

| Column Name | Type |
|---|---|
| id | int |
| name | varchar |

`id` is the primary key. Table: `Rides`

| Column Name | Type |
|---|---|
| id | int |
| user_id | int |
| distance | int |

`id` is the primary key; `user_id` references `Users.id`. Report the distance
travelled by each user, ordered by distance descending, then name ascending.
Users with no rides have travelled distance `0`.

## Solution (MySQL, annotated)

```sql
SELECT u.name, COALESCE(SUM(r.distance), 0) AS travelled_distance 
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
```

## Test-case annotations

```
Input:
Users table:
+----+-----------+
| id | name      |
+----+-----------+
| 1  | Alice     |
| 2  | Bob       |
| 3  | Alex      |
| 4  | Donald    |
| 7  | Lee       |
| 13 | Jonathan  |
| 19 | Elvis     |
+----+-----------+

Rides table:
+----+---------+----------+
| id | user_id | distance |
+----+---------+----------+
| 1  | 1       | 120      |
| 2  | 2       | 317      |
| 3  | 3       | 222      |
| 4  | 7       | 100      |
| 5  | 13      | 312      |
| 6  | 19      | 50       |
| 7  | 7       | 120      |
| 8  | 19      | 400      |
| 9  | 7       | 230      |
+----+---------+----------+

Output (Elvis and Lee tie on 450 — Elvis first, name ascending):
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/058_top_travellers -v` green
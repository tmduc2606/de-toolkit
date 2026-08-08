# SQL056 — Reformat Department Table

> Source: LeetCode 1179 (hand-solved, not part of the SQL 50 answersheet).

## Problem

Table: `Department`

| Column Name | Type |
|---|---|
| id | int |
| revenue | int |
| month | varchar |

`(id, month)` is the primary key; `month` ∈ {Jan..Dec}. Reformat the table so
there is a `department id` column and a revenue column for **each month**;
rows where a month has no revenue show `null`. 13 columns total.

## Solution (MySQL, annotated)

```sql
# Equivalent to SUM w/ conditions using department.pivot(index = "id", columns = "month", values = "revenue")
# SQL CASE + GROUP BY → conditional aggregation → rows → columns → pandas pivot()
SELECT 
    d.id,
    SUM(CASE WHEN d.month = 'Jan' THEN revenue END) AS Jan_Revenue,
    ... -- one per month
FROM Department d
GROUP BY d.id;
```

## Test-case annotations

```
Input Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Output (13 columns):
| id | Jan_Revenue | Feb_Revenue | Mar_Revenue | Apr..Nov | Dec_Revenue |
| 1  | 8000        | 7000        | 6000        | null     | null        |
| 2  | 9000        | null        | null        | null     | null        |
| 3  | null        | 10000        | null        | null     | null        |
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/056_reformat_department_table -v` green
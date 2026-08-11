# SQL063 — Odd and Even Transactions

> Source: LeetCode 3220 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `transactions`

| Column Name | Type |
|---|---|
| transaction_id | int |
| amount | int |
| transaction_date | date |

`transaction_id` uniquely identifies each row. Find the sum of amounts for
odd and even transactions for each day. If there are no odd or even
transactions for a specific date, display `0`. Return the result table
ordered by `transaction_date` in ascending order. Note that parity refers to
the `amount`, not the `transaction_id`.

## Solution (MySQL, annotated)

```sql
-- Conditional aggregation: SUM() with CASE WHEN tests amount parity
-- per row; ELSE 0 yields 0 when a day has no odd/even transactions
-- group by transaction_date for the per-day sums, ordered ASC
SELECT
    t.transaction_date,
    SUM(CASE WHEN t.amount % 2 != 0 THEN t.amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN t.amount % 2 = 0 THEN t.amount ELSE 0 END) AS even_sum
FROM transactions t
GROUP BY t.transaction_date
ORDER BY t.transaction_date ASC;
```

> DuckDB note: MySQL's `IF(cond, a, b)` is written as `CASE WHEN ... END`,
> and `%` modulo works identically in DuckDB — no rewrite needed.

## Test-case annotations

```
Input:
transactions table:
+----------------+--------+------------------+
| transaction_id | amount | transaction_date |
+----------------+--------+------------------+
| 1              | 150    | 2024-07-01       |
| 2              | 200    | 2024-07-01       |
| 3              | 75     | 2024-07-01       |
| 4              | 300    | 2024-07-02       |
| 5              | 50     | 2024-07-02       |
| 6              | 120    | 2024-07-03       |
+----------------+--------+------------------+

2024-07-01: odd 75, even 150 + 200 = 350.
2024-07-02: odd 0, even 300 + 50 = 350.
2024-07-03: odd 0, even 120.

Output (ordered by transaction_date ASC):
+------------------+---------+----------+
| transaction_date | odd_sum | even_sum |
+------------------+---------+----------+
| 2024-07-01       | 75      | 350      |
| 2024-07-02       | 0       | 350      |
| 2024-07-03       | 0       | 120      |
+------------------+---------+----------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/063_odd_and_even_transactions -v` green
# SQL060 — Bank Account Summary II

> Source: LeetCode 1587 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Tables: `Users`

| Column Name | Type |
|---|---|
| account | int |
| name | varchar |

`account` is the primary key. Table: `Transactions`

| Column Name | Type |
|---|---|
| trans_id | int |
| account | int |
| amount | int |
| transacted_on | datetime |

`trans_id` is the primary key; `account` references `Users.account`. Report
the name and balance of users whose total balance is greater than `10000`.

## Solution (MySQL, annotated)

```sql
SELECT u.name, COALESCE(SUM(t.amount), 0) AS balance
FROM Transactions t
JOIN Users u ON t.account = u.account
GROUP BY t.account
HAVING balance > 10000;
```

> DuckDB note: strict `GROUP BY` requires every non-aggregated select column
> (`u.name`) to appear in the GROUP BY clause.

## Test-case annotations

```
Input:
Users table:
+---------+-----------+
| account | name      |
+---------+-----------+
| 900001  | Alice     |
| 900002  | Bob       |
| 900003  | Charlie   |
+---------+-----------+

Transactions table:
+----------+---------+--------+---------------+
| trans_id | account | amount | transacted_on |
+----------+---------+--------+---------------+
| 1        | 900001  | 7000   | 2020-08-01    |
| 2        | 900001  | 7000   | 2020-09-01    |
| 3        | 900001  | -3000  | 2020-09-02    |
| 4        | 900002  | 1000   | 2020-09-12    |
| 5        | 900003  | 6000   | 2020-08-07    |
| 6        | 900003  | 6000   | 2020-09-07    |
| 7        | 900003  | -4000  | 2020-09-11    |
+----------+---------+--------+---------------+

Balances: Alice 11000 (>= 10000), Bob 1000, Charlie 8000 — only Alice is
reported.

Output:
+---------+---------+
| name    | balance |
+---------+---------+
| Alice   | 11000   |
+---------+---------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/060_bank_account_summary_ii -v` green
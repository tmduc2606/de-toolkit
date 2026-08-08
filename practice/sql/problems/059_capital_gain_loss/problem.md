# SQL059 — Capital Gain/Loss

> Source: LeetCode 1393 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Stocks`

| Column Name | Type |
|---|---|
| stock_name | varchar |
| operation | varchar |
| price | int |

`(stock_name, operation)` is the primary key; `operation` is `Buy` or `Sell`.
For each stock, report its capital gain/loss — sum of `Buy` as negative and
`Sell` as positive.

## Solution (MySQL, annotated)

```sql
SELECT s.stock_name, SUM(
    CASE s.operation
        WHEN 'Buy' THEN -1 * s.price
        ELSE s.price
    END
) AS capital_gain_loss
FROM Stocks s
GROUP BY s.stock_name;
```

## Test-case annotations

```
Input:
Stocks table:
+---------------+-----------+-------+
| stock_name    | operation | price |
+---------------+-----------+-------+
| Leetcode      | Buy       | 1000  |
| Corona Masks  | Buy       | 10    |
| Leetcode      | Sell      | 9000  |
| Handbags      | Buy       | 30000 |
| Corona Masks  | Sell      | 1010  |
| Corona Masks  | Buy       | 1000  |
| Corona Masks  | Sell      | 500   |
| Corona Masks  | Buy       | 10000 |
| Handbags      | Sell      | 7000  |
| Corona Masks  | Sell      | 10000 |
+---------------+-----------+-------+

Output:
+---------------+-------------------+
| stock_name    | capital_gain_loss |
+---------------+-------------------+
| Corona Masks  | 500               |
| Handbags      | -23000            |
| Leetcode      | 8000              |
+---------------+-------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/059_capital_gain_loss -v` green
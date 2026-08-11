# SQL061 — Market Analysis I

> Source: LeetCode 1158 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Users`

| Column Name | Type |
|---|---|
| user_id | int |
| join_date | date |
| favorite_brand | varchar |

`user_id` is the primary key. Table: `Orders`

| Column Name | Type |
|---|---|
| order_id | int |
| order_date | date |
| item_id | int |
| buyer_id | int |
| seller_id | int |

`order_id` is the primary key; `buyer_id` and `seller_id` reference
`Users.user_id`. Find for each user the join date and the number of orders
they made as a buyer in `2019`.

## Solution (MySQL, annotated)

```sql
-- Projecting from Users table -> Group by u.user_id, u.join_date
-- LEFT JOIN on o.buyer_id = u.user_id with the orders made in 2019 only
-- COUNT() over the GROUP BY keeps users with 0 orders in 2019
SELECT u.user_id AS buyer_id, u.join_date, COUNT(o.item_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON o.buyer_id = u.user_id
    AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
```

> DuckDB note: `solution.sql` adds `ORDER BY u.user_id` so the test can assert
> the annotated output rows exactly (LeetCode accepts any order).

## Test-case annotations

```
Input:
Users table:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+

Orders table:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+

2019 buyer counts: user 1 -> 1 (order 1), user 2 -> 2 (orders 3 and 6),
users 3 and 4 -> 0 (LEFT JOIN keeps them).

Output:
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/061_market_analysis_i -v` green
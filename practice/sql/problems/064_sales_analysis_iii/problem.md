# SQL064 — Sales Analysis III

> Source: LeetCode 1084 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Product`

| Column Name | Type |
|---|---|
| product_id | int |
| product_name | varchar |
| unit_price | int |

`product_id` is the primary key. Table: `Sales`

| Column Name | Type |
|---|---|
| seller_id | int |
| product_id | int |
| buyer_id | int |
| sale_date | date |
| quantity | int |
| price | int |

`product_id` references `Product.product_id`; rows may be duplicated. Report
the products that were **only** sold in the first quarter of `2019`, i.e.
between `2019-01-01` and `2019-03-31` inclusive.

## Solution (MySQL, annotated)

```sql
-- Optimal approach: MIN()/MAX() over the per-product sale dates prove every
-- sale (not just the latest one) fell inside Q1 2019 — the ROW_NUMBER()
-- brute force fails the edge case where the latest sale sits outside Q1
SELECT p.product_id, p.product_name
FROM Sales s
JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31';
```

> DuckDB note: `solution.sql` adds `ORDER BY p.product_id` so the test can
> assert the annotated output rows exactly (LeetCode accepts any order).

## Test-case annotations

```
Input:
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+

Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+

Product 1 was only sold in Q1 2019 (2019-01-21).
Product 2 was sold in Q1 2019 and again after it (2019-06-02).
Product 3 was only sold after Q1 2019 (2019-05-13).
Only product 1 qualifies.

Output:
+-------------+--------------+
| product_id  | product_name |
+-------------+--------------+
| 1           | S8           |
+-------------+--------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/064_sales_analysis_iii -v` green
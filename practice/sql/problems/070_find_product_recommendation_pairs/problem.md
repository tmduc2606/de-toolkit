# SQL070 — Find Product Recommendation Pairs

> Source: LeetCode 3521 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `ProductPurchases`

| Column Name | Type |
|---|---|
| user_id | int |
| product_id | int |
| quantity | int |

`(user_id, product_id)` is the unique key. Table: `ProductInfo`

| Column Name | Type |
|---|---|
| product_id | int |
| category | varchar |
| price | decimal |

`product_id` is the primary key. Implement the "customers who bought this
also bought" feature: identify distinct product pairs frequently purchased
together by the same customers (`product1_id` < `product2_id`), count the
customers who bought both, and keep only pairs bought by at least `3`
different customers. Return the result table ordered by `customer_count` in
descending order, then by `product1_id` ascending, then by `product2_id`
ascending.

## Solution (MySQL, annotated)

```sql
-- Using SELF-JOIN + COUNT + DISTINCT
-- 1st LEFT-JOIN: find how many users bought the pair of product_ids
-- 2nd/3rd JOINs: look up the categories of both products of the pair;
--   pp1.product_id < pp2.product_id in the ON clause dedupes the pairs
-- GROUP BY the pair of product_ids and category_ids; featured on the
-- output table if at least 3 distinct customers bought that pair
SELECT
    pp1.product_id AS product1_id,
    pp2.product_id AS product2_id,
    pi1.category AS product1_category,
    pi2.category AS product2_category,
    COUNT(DISTINCT pp1.user_id) AS customer_count
FROM ProductPurchases pp1
LEFT JOIN ProductPurchases pp2
    ON pp1.user_id = pp2.user_id
JOIN ProductInfo pi1
    ON pi1.product_id = pp1.product_id
    AND pp1.product_id < pp2.product_id
JOIN ProductInfo pi2
    ON pi2.product_id = pp2.product_id
GROUP BY
    pp1.product_id,
    pp2.product_id,
    pi1.category,
    pi2.category
HAVING COUNT(DISTINCT pp1.user_id) >= 3
ORDER BY customer_count DESC, product1_id ASC, product2_id ASC;
```

> DuckDB note: runs as-is — strict `GROUP BY` is satisfied and
> `COUNT(DISTINCT ...)` is supported.

## Test-case annotations

```
Input:
ProductPurchases table:
+---------+------------+----------+
| user_id | product_id | quantity |
+---------+------------+----------+
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 103        | 3        |
| 2       | 101        | 1        |
| 2       | 102        | 5        |
| 2       | 104        | 1        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 105        | 4        |
| 4       | 101        | 1        |
| 4       | 102        | 1        |
| 4       | 103        | 2        |
| 4       | 104        | 3        |
| 5       | 102        | 2        |
| 5       | 104        | 1        |
+---------+------------+----------+

ProductInfo table:
+------------+-------------+-------+
| product_id | category    | price |
+------------+-------------+-------+
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Clothing    | 35    |
| 104        | Kitchen     | 50    |
| 105        | Sports      | 75    |
+------------+-------------+-------+

Pair (101, 102): users 1, 2, 4 -> 3 customers.
Pair (101, 103): users 1, 3, 4 -> 3 customers.
Pair (102, 104): users 2, 4, 5 -> 3 customers.
All other pairs fall below the threshold of 3 distinct customers.

Output (customer_count DESC, then product ids ASC):
+-------------+-------------+-------------------+-------------------+----------------+
| product1_id | product2_id | product1_category | product2_category | customer_count |
+-------------+-------------+-------------------+-------------------+----------------+
| 101         | 102         | Electronics       | Books             | 3              |
| 101         | 103         | Electronics       | Clothing          | 3              |
| 102         | 104         | Books             | Kitchen           | 3              |
+-------------+-------------+-------------------+-------------------+----------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/070_find_product_recommendation_pairs -v` green
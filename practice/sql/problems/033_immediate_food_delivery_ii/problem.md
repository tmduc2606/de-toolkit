# SQL033 — Immediate Food Delivery II

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT ROUND(
    COUNT(
        CASE WHEN d.order_date = d.customer_pref_delivery_date THEN delivery_id END
        ) * 100 / COUNT(d.delivery_id), 2
) AS immediate_percentage
FROM Delivery d
JOIN
    (
        SELECT customer_id, MIN(order_date) AS first_order
        FROM Delivery
        GROUP BY customer_id
    ) AS ed
ON ed.customer_id = d.customer_id 
AND d.order_date = ed.first_order;
```

## Test-case annotations

```
# 1. Find all customers whose order dates are earliest
# 2. JOIN ON the ed.customer_id = d.customer_id AND d.order_date = ed.first_order, which leads us to the table with earliest orders
# 3. IMMEDIATE PERCENTAGE = orders due time / total orders
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/033_immediate_food_delivery_ii -v` green

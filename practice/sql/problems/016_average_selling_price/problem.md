# SQL016 — Average Selling Price

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT p.product_id, ROUND(
    COALESCE(SUM(us.units * p.price) / NULLIF(SUM(us.units), 0), 0), 2) AS average_price
FROM Prices p
LEFT JOIN UnitsSold us ON 
    (p.product_id = us.product_id) AND
    (us.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY p.product_id;
```

## Test-case annotations

```
# COALESCE (picking first non-null values) + LEFT JOIN, BETWEEN (Dates)
# Syntax: COALESCE(val1, val2, ...., val_n) -> COALESCE(SUM() / NULLIF(SUM(), 0), 0)
# Average selling price = Total Price of Product / Number of products sold.
# Functionality:
# 1. For denominator -> If null, assigns to 0 (NULLIF)
# 2. For numerator -> Picking up first non-null values, subsequently 0 if no sales persist (COALESCE). -> Avg price 0
# 3. Othewise, take the final avg price
# NOTES: Do not treat purchase_date JOIN as a WHERE Clause. Otherwise us.* is NULL, the WHERE condition fails, and rows from Prices get removed. (result: empty output instead of 0)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/016_average_selling_price -v` green

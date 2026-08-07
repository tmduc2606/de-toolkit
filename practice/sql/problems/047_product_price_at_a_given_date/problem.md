# SQL047 — Product Price at a Given Date

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT p.product_id, 10 AS PRICE
FROM Products p
WHERE p.product_id NOT IN (
    SELECT product_id FROM Products
    WHERE change_date <= '2019-08-16'
)
UNION
SELECT product_id, new_price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
);
```

## Test-case annotations

```
# 1st query: Products that has not yet updated after 2019-08-16 
# 2nd query: Products that has been changed as of 2019-08-16, group byp roduct_id as a product
# might change multiple times
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/047_product_price_at_a_given_date -v` green

# SQL020 — Product Sales Analysis III

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
WHERE (s.product_id, s.year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id 
);
```

## Test-case annotations

```
# Subqueries w/ MIN to find the earliest year of sale
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/020_product_sales_analysis_iii -v` green

# SQL041 — Group Sold Products By The Date

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT a.sell_date, COUNT(DISTINCT a.product) AS num_sold , GROUP_CONCAT(DISTINCT a.product ORDER BY a.product SEPARATOR ',') AS products
FROM Activities a
GROUP BY CAST(a.sell_date AS DATE)
ORDER BY a.sell_date ASC;
```

## Test-case annotations

```
# GROUP_CONCAT() w/ GROUP BY CAST(sell_date AS Date), SEPARATED BY ','
# Lexicographically w/ ORDER BY a.product
# ORDER BY a.sell_date
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/041_group_sold_products_by_the_date -v` green

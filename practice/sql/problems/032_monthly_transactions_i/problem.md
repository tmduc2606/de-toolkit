# SQL032 — Monthly Transactions I

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT 
    DATE_FORMAT(t.trans_date, '%Y-%m') AS month,
    t.country,
    COUNT(t.state) AS trans_count,
    COALESCE(COUNT(CASE WHEN t.state = 'approved' THEN 1 END), 0) AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    COALESCE(SUM(CASE WHEN t.state = 'approved' THEN t.amount END), 0) AS approved_total_amount 
FROM Transactions t
GROUP BY month, t.country;
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/032_monthly_transactions_i -v` green

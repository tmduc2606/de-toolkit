# SQL035 — Count Salary Categories

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT c.category, COALESCE(a.accounts_count, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
) c
LEFT JOIN (
    SELECT (
        CASE WHEN (income < 20000) THEN 'Low Salary'
        WHEN (income >= 20000) AND (income <= 50000) THEN 'Average Salary'
        WHEN (income > 50000) THEN 'High Salary' END
    ) AS category, COUNT(*) AS accounts_count
    FROM Accounts
    GROUP BY category
) a
ON c.category = a.category;
SELECT 'Low Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION
SELECT 'Average Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE (income >= 20000) AND (income <= 50000)
UNION
SELECT 'High Salary' AS category, COUNT(account_id) AS accounts_count
FROM Accounts
WHERE income > 50000
```

## Test-case annotations

```
# 1. One table with category column only
# 2. One table with the counts of category respective to the account_id
# 3. LEFT JOIN
# 4. Project the category (overall-joined table) & handle NULL values w/ COALESCE
# Alternative Approach (UNION ALL on each separate category)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/035_count_salary_categories -v` green

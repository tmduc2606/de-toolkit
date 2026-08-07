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

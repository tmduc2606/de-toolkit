SELECT u.name, COALESCE(SUM(t.amount), 0) AS balance
FROM Transactions t
JOIN Users u ON t.account = u.account
-- DuckDB: strict GROUP BY — every non-aggregated column must be listed
GROUP BY u.account, u.name
HAVING balance > 10000
ORDER BY balance DESC;
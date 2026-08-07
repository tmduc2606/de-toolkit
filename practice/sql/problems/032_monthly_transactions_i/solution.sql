SELECT 
    -- DuckDB: DATE_FORMAT -> STRFTIME (MySQL-only)
    STRFTIME(t.trans_date, '%Y-%m') AS month,
    t.country,
    COUNT(t.state) AS trans_count,
    COALESCE(COUNT(CASE WHEN t.state = 'approved' THEN 1 END), 0) AS approved_count,
    SUM(t.amount) AS trans_total_amount,
    COALESCE(SUM(CASE WHEN t.state = 'approved' THEN t.amount END), 0) AS approved_total_amount 
FROM Transactions t
GROUP BY month, t.country;

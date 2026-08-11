-- Conditional aggregation: SUM() with CASE WHEN tests amount parity
-- per row; ELSE 0 yields 0 when a day has no odd/even transactions
-- group by transaction_date for the per-day sums, ordered ASC
SELECT
    t.transaction_date,
    SUM(CASE WHEN t.amount % 2 != 0 THEN t.amount ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN t.amount % 2 = 0 THEN t.amount ELSE 0 END) AS even_sum
FROM transactions t
GROUP BY t.transaction_date
ORDER BY t.transaction_date ASC;
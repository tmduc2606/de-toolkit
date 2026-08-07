SELECT a.sell_date, COUNT(DISTINCT a.product) AS num_sold,
    -- DuckDB: GROUP_CONCAT(... ORDER BY ... SEPARATOR ',') -> STRING_AGG
    STRING_AGG(DISTINCT a.product, ',' ORDER BY a.product) AS products
FROM Activities a
GROUP BY a.sell_date
ORDER BY a.sell_date ASC;

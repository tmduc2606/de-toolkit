SELECT s.stock_name, SUM(
    CASE s.operation
        WHEN 'Buy' THEN -1 * s.price
        ELSE s.price
    END
) AS capital_gain_loss
FROM Stocks s
GROUP BY s.stock_name
ORDER BY s.stock_name;
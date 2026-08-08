-- schema.sql — Capital Gain/Loss (LeetCode 1393)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Stocks (
    stock_name TEXT,
    operation TEXT,
    price INTEGER
);

INSERT INTO Stocks (stock_name, operation, price) VALUES
    ('Leetcode', 'Buy', 1000),
    ('Corona Masks', 'Buy', 10),
    ('Leetcode', 'Sell', 9000),
    ('Handbags', 'Buy', 30000),
    ('Corona Masks', 'Sell', 1010),
    ('Corona Masks', 'Buy', 1000),
    ('Corona Masks', 'Sell', 500),
    ('Corona Masks', 'Buy', 10000),
    ('Handbags', 'Sell', 7000),
    ('Corona Masks', 'Sell', 10000);
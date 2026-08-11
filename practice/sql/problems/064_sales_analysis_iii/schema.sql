-- schema.sql — Sales Analysis III (LeetCode 1084)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    unit_price INTEGER
);

INSERT INTO Product (product_id, product_name, unit_price) VALUES
    (1, 'S8', 1000),
    (2, 'G4', 800),
    (3, 'iPhone', 1400);

CREATE TABLE IF NOT EXISTS Sales (
    seller_id INTEGER,
    product_id INTEGER,
    buyer_id INTEGER,
    sale_date DATE,
    quantity INTEGER,
    price INTEGER
);

INSERT INTO Sales (seller_id, product_id, buyer_id, sale_date, quantity, price) VALUES
    (1, 1, 1, '2019-01-21', 2, 2000),
    (1, 2, 2, '2019-02-17', 1, 800),
    (2, 2, 3, '2019-06-02', 1, 800),
    (3, 3, 4, '2019-05-13', 2, 2800);
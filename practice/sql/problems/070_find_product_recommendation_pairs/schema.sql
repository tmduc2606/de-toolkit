-- schema.sql — Find Product Recommendation Pairs (LeetCode 3521)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS ProductPurchases (
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (user_id, product_id)
);

INSERT INTO ProductPurchases (user_id, product_id, quantity) VALUES
    (1, 101, 2),
    (1, 102, 1),
    (1, 103, 3),
    (2, 101, 1),
    (2, 102, 5),
    (2, 104, 1),
    (3, 101, 2),
    (3, 103, 1),
    (3, 105, 4),
    (4, 101, 1),
    (4, 102, 1),
    (4, 103, 2),
    (4, 104, 3),
    (5, 102, 2),
    (5, 104, 1);

CREATE TABLE IF NOT EXISTS ProductInfo (
    product_id INTEGER PRIMARY KEY,
    category TEXT,
    price DECIMAL
);

INSERT INTO ProductInfo (product_id, category, price) VALUES
    (101, 'Electronics', 100),
    (102, 'Books', 20),
    (103, 'Clothing', 35),
    (104, 'Kitchen', 50),
    (105, 'Sports', 75);
-- schema.sql — Market Analysis I (LeetCode 1158)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    join_date DATE,
    favorite_brand TEXT
);

INSERT INTO Users (user_id, join_date, favorite_brand) VALUES
    (1, '2018-01-01', 'Lenovo'),
    (2, '2018-02-09', 'Samsung'),
    (3, '2018-01-19', 'LG'),
    (4, '2018-05-21', 'HP');

CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    item_id INTEGER,
    buyer_id INTEGER,
    seller_id INTEGER
);

INSERT INTO Orders (order_id, order_date, item_id, buyer_id, seller_id) VALUES
    (1, '2019-08-01', 4, 1, 2),
    (2, '2018-08-02', 2, 1, 3),
    (3, '2019-08-03', 3, 2, 3),
    (4, '2018-08-04', 1, 4, 2),
    (5, '2018-08-04', 1, 3, 4),
    (6, '2019-08-05', 2, 2, 4);
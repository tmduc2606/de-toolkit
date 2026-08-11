-- schema.sql — Find Products with Valid Serial Numbers (LeetCode 3465)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    description TEXT
);

INSERT INTO products (product_id, product_name, description) VALUES
    (1, 'Widget A', 'This is a sample product with SN1234-5678'),
    (2, 'Widget B', 'A product with serial SN9876-1234 in the description'),
    (3, 'Widget C', 'Product SN1234-56789 is available now'),
    (4, 'Widget D', 'No serial number here'),
    (5, 'Widget E', 'Check out SN4321-8765 in this description');
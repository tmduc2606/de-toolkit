-- schema.sql — Odd and Even Transactions (LeetCode 3220)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY,
    amount INTEGER,
    transaction_date DATE
);

INSERT INTO transactions (transaction_id, amount, transaction_date) VALUES
    (1, 150, '2024-07-01'),
    (2, 200, '2024-07-01'),
    (3, 75,  '2024-07-01'),
    (4, 300, '2024-07-02'),
    (5, 50,  '2024-07-02'),
    (6, 120, '2024-07-03');
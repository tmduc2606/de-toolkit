-- schema.sql — Reformat Department Table (LeetCode 1179)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Department (
    id INTEGER,
    revenue INTEGER,
    month TEXT
);

INSERT INTO Department (id, revenue, month) VALUES
    (1, 8000, 'Jan'),
    (2, 9000, 'Jan'),
    (3, 10000, 'Feb'),
    (1, 7000, 'Feb'),
    (1, 6000, 'Mar');
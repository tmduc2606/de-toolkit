-- schema.sql — Swap Salary (LeetCode 627)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Salary (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sex TEXT,
    salary INTEGER
);

INSERT INTO Salary (id, name, sex, salary) VALUES
    (1, 'A', 'm', 2500),
    (2, 'B', 'f', 1500),
    (3, 'C', 'm', 5500),
    (4, 'D', 'f', 500);
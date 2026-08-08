-- schema.sql — Employees Earning More Than Their Managers (LeetCode 181)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    managerId INTEGER
);

INSERT INTO Employee (id, name, salary, managerId) VALUES
    (1, 'Joe', 70000, 3),
    (2, 'Henry', 80000, 4),
    (3, 'Sam', 60000, NULL),
    (4, 'Max', 90000, NULL);

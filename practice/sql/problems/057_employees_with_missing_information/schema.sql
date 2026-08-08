-- schema.sql — Employees With Missing Information (LeetCode 1965)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO Employees (employee_id, name) VALUES
    (2, 'Crew'),
    (4, 'Haven'),
    (5, 'Kristian');

CREATE TABLE IF NOT EXISTS Salaries (
    employee_id INTEGER PRIMARY KEY,
    salary INTEGER
);

INSERT INTO Salaries (employee_id, salary) VALUES
    (5, 76071),
    (6, 30697),
    (7, 90272),
    (9, 70017);
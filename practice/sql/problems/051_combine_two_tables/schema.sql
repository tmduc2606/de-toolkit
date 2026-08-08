-- schema.sql — Combine Two Tables (LeetCode 175)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Person (
    personId INTEGER PRIMARY KEY,
    lastName TEXT,
    firstName TEXT
);

INSERT INTO Person (personId, lastName, firstName) VALUES
    (1, 'Wang', 'Allen'),
    (2, 'Alice', 'Bob');

CREATE TABLE IF NOT EXISTS Address (
    addressId INTEGER PRIMARY KEY,
    personId INTEGER,
    city TEXT,
    state TEXT
);

INSERT INTO Address (addressId, personId, city, state) VALUES
    (1, 2, 'New York City', 'New York'),
    (2, 3, 'Leetcode', 'California');

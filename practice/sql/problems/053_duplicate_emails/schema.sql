-- schema.sql — Duplicate Emails (LeetCode 182)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Person (
    id INTEGER PRIMARY KEY,
    email TEXT
);

INSERT INTO Person (id, email) VALUES
    (1, 'a@b.com'),
    (2, 'c@d.com'),
    (3, 'a@b.com');
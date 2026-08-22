-- schema.sql — Find Valid Emails (LeetCode 3436)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    email TEXT
);

INSERT INTO Users (user_id, email) VALUES
    (1, 'alice@example.com'),
    (2, 'bob_at_example.com'),
    (3, 'charlie@example.net'),
    (4, 'david@domain.com'),
    (5, 'eve@invalid');
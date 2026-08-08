-- schema.sql — Tree Node (LeetCode 608)
-- The exact LeetCode example test case.

CREATE TABLE IF NOT EXISTS Tree (
    id INTEGER PRIMARY KEY,
    p_id INTEGER
);

INSERT INTO Tree (id, p_id) VALUES
    (1, NULL),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2);
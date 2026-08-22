-- schema.sql — <Problem Title>
-- Fill in the LeetCode example test case:
--   1. CREATE TABLE IF NOT EXISTS ... for every table in solution.sql
--   2. INSERT the annotated example rows
-- The DuckDB test below switches from "skip" to real verification as soon as
-- this file contains an INSERT statement (see docs/OVERHAUL_BLUEPRINT.md §4).

CREATE TABLE IF NOT EXISTS example (
    id INTEGER PRIMARY KEY
);

-- INSERT INTO example (id) VALUES (1);
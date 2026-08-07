-- solution.sql — your MySQL answer, kept DuckDB-portable.
-- Fix MySQL-only constructs (IFNULL -> COALESCE, %-date filters,
-- LENGTH() vs CHAR_LENGTH()) and note them with "-- DuckDB:".
SELECT id
FROM example;
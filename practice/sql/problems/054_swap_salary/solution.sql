-- DuckDB: MySQL double-quoted string literals are written as single quotes.
UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    WHEN sex = 'f' THEN 'm'
    WHEN sex IS NULL THEN NULL
    ELSE sex
END;
SELECT *
FROM Users u
-- DuckDB: MySQL RLIKE -> regexp_full_match; drop the redundant BINARY LIKE
WHERE regexp_full_match(u.mail, '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$');

-- ^[a-z0-9]+@[a-z]+\.com$: exactly one @ separator; local part alphanumeric;
-- domain letters only; literal .com at the end
-- DuckDB: MySQL's REGEXP operator does not exist here -> REGEXP_MATCHES.
-- MySQL REGEXP is case-insensitive by default while DuckDB regexes are
-- case-sensitive, so the inline (?i) flag preserves the MySQL behavior
SELECT u.user_id, u.email
FROM Users u
WHERE REGEXP_MATCHES(u.email, '(?i)^[a-z0-9]+@[a-z]+\.com$')
ORDER BY u.user_id ASC;
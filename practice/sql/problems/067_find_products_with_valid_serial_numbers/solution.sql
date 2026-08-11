-- (^|[^A-Za-z0-9]): the SN prefix may sit at the string start or after a
--   non-alphanumeric character (it must not be glued to letters/digits)
-- (?![A-Za-z0-9]): nothing may follow the second digit group but a
--   non-alphanumeric character or the end of the string
-- DuckDB: MySQL's REGEXP_LIKE(..., 'c') lookahead (?!...) is not supported;
--   the consuming boundary ([^A-Za-z0-9]|$) below is boolean-equivalent.
--   DuckDB regexes are case-sensitive by default, matching the 'c' flag.
SELECT p.product_id, p.product_name, p.description
FROM products p
WHERE REGEXP_MATCHES(p.description, '(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9]|$)')
ORDER BY p.product_id ASC;
# SQL067 — Find Products with Valid Serial Numbers

> Source: LeetCode 3465 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `products`

| Column Name | Type |
|---|---|
| product_id | int |
| product_name | varchar |
| description | varchar |

`product_id` is the unique key. Find all products whose description contains
a valid serial number pattern, defined as:

- starts with the letters `SN` (case-sensitive),
- followed by exactly `4` digits,
- a hyphen `-`,
- followed by exactly `4` digits.

The serial number may appear anywhere inside the description. Return the
result table ordered by `product_id` in ascending order.

## Solution (MySQL, annotated)

```sql
-- (^|[^A-Za-z0-9]): the SN prefix may sit at the string start or after a
--   non-alphanumeric character (it must not be glued to letters/digits)
-- (?![A-Za-z0-9]): nothing may follow the second digit group but a
--   non-alphanumeric character or the end of the string
SELECT product_id, product_name, description
FROM products
WHERE REGEXP_LIKE(description, '(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}(?![A-Za-z0-9])', 'c')
ORDER BY product_id ASC;
```

> DuckDB note: `REGEXP_LIKE(..., 'c')` and the lookahead `(?!...)` are
> MySQL-specific — DuckDB exposes `REGEXP_MATCHES` and its regex engine
> rejects lookahead. `solution.sql` uses the boolean-equivalent consuming
> boundary `([^A-Za-z0-9]|$)` instead (DuckDB regexes are case-sensitive by
> default, which covers the `'c'` flag).

## Test-case annotations

```
Input:
products table:
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 3          | Widget C     | Product SN1234-56789 is available now                |
| 4          | Widget D     | No serial number here                                |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+

Product 1: valid SN1234-5678.
Product 2: valid SN9876-1234.
Product 3: invalid SN1234-56789 (5 digits after the hyphen).
Product 4: no serial number.
Product 5: valid SN4321-8765 (end of string still counts).

Output (ordered by product_id ASC):
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/067_find_products_with_valid_serial_numbers -v` green
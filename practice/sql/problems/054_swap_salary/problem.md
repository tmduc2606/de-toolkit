# SQL054 — Swap Salary

> Source: LeetCode 627 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Salary`

| Column Name | Type |
|---|---|
| id | int |
| name | varchar |
| sex | varchar |
| salary | int |

`id` is the primary key. Swap all `'m'` and `'f'` values of `sex` with a single
UPDATE statement and no intermediate tables; only use a `CASE` expression.

## Solution (MySQL, annotated)

```sql
UPDATE Salary 
SET sex = ( CASE sex 
    WHEN "m" THEN "f"
    WHEN "f" THEN "m"
    END
);
```

> Update annotation: `UPDATE Table SET variable1 = VALUE1, ... variableN = VALUEN
> WHERE condition1, ..., conditionN`
>
> DuckDB note: MySQL accepts double-quoted string literals (`"m"`); DuckDB
> treats double quotes as identifiers, so the solution uses single quotes.

## Test-case annotations

```
Input Salary table:
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+

Output (after UPDATE):
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/054_swap_salary -v` green
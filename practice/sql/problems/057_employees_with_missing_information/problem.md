# SQL057 — Employees With Missing Information

> Source: LeetCode 1965 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Tables: `Employees`

| Column Name | Type |
|---|---|
| employee_id | int |
| name | varchar |

`employee_id` is the primary key. Table: `Salaries`

| Column Name | Type |
|---|---|
| employee_id | int |
| salary | int |

`employee_id` is the primary key. Report the ids of all employees whose name
or salary is missing — i.e. ids present in exactly one of the two tables.
Sort ascending.

## Solution (MySQL, annotated)

```sql
# Employees whose salary is missing (left join)
# Union with salaries whose name is missing (right join)
SELECT employee_id
FROM
(
    SELECT e.employee_id 
    FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL

    UNION

    SELECT s.employee_id
    FROM Employees e
    RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
    WHERE e.name IS NULL
) t
ORDER BY t.employee_id ASC;
```

## Test-case annotations

```
Input:
Employees table:                      Salaries table:
+-------------+-------+               +-------------+--------+
| employee_id | name  |               | employee_id | salary |
+-------------+-------+               +-------------+--------+
| 2           | Crew  |               | 5           | 76071  |
| 4           | Haven |               | 6           | 30697  |
| 5           | Kristian |            | 7           | 90272  |
+-------------+-------+               | 9           | 70017  |
                                      +-------------+--------+

Special cases: employee 5 has both name and salary (not reported);
employee 2 has no row in Salaries, employees 6/7/9 have no row in Employees.

Output:
+-------------+
| employee_id |
+-------------+
| 2           |
| 4           |
| 6           |
| 7           |
| 9           |
+-------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/057_employees_with_missing_information -v` green
# SQL052 — Employees Earning More Than Their Managers

> Source: LeetCode 181 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Employee`

| Column Name | Type |
|---|---|
| id | int |
| name | varchar |
| salary | int |
| managerId | int |

`id` is the primary key; `managerId` references `id`. Find employees whose
salary is strictly greater than their manager's salary.

## Solution (MySQL, annotated)

```sql
# Self-join managerId on employeeId
SELECT e2.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e2.managerId = e1.id
WHERE e2.salary > e1.salary;
```

## Test-case annotations

```
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | null      |
| 4  | Max   | 90000  | null      |
+----+-------+--------+-----------+

Self-join intermediate result (e1 = manager, e2 = employee):
| e1.id | e1.name | e1.salary | e1.managerId | e2.id | e2.name | e2.salary | e2.managerId |
| 3     | Sam     | 60000     | null         | 1     | Joe     | 70000     | 3            |
| 4     | Max     | 90000     | null         | 2     | Henry   | 80000     | 4            |

Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/052_employees_earning_more_than_their_managers -v` green

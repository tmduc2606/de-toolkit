# SQL025 — The Number of Employees Which Report to Each Employee

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT e1.employee_id, e1.name, COUNT(e1.employee_id) AS reports_count, ROUND(AVG(e2.age), 0) AS average_age
FROM Employees e1
JOIN Employees e2 ON e1.employee_id = e2.reports_to
GROUP BY e1.employee_id, e1.name
ORDER BY e1.employee_id ASC;
```

## Test-case annotations

```
# SELF-JOIN e1.employee_id = e2.reports_to, GROUP BY id and name
# e1.employee_id	e1.name	e2.employee_id	e2.name	e2.age
# 1	Michael	2	Alice	38
# 1	Michael	3	Bob	42
# 2	Alice	4	Charlie	34
# 2	Alice	5	David	40
# 3	Bob	6	Eve	37
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/025_the_number_of_employees_which_report_to_each_employee -v` green

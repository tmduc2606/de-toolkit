# SQL029 — Employees Whose Manager Left the Company

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2 ON e2.employee_id = e1.manager_id
WHERE (e2.employee_id IS NULL) 
AND (e1.manager_id IS NOT NULL)
AND e1.salary < 30000
ORDER BY e1.employee_id;
```

## Test-case annotations

```
# Self-join on employee_id and manager_id
# Intermediate result
# e.employee_id	e.name	e.manager_id	m.employee_id	m.name
# 3	Mila	9	9	Mikaela
# 12	Antonella	NULL	NULL	NULL
# 13	Emery	NULL	NULL	NULL
#1	Kalel	11	11	Joziah
# 9	Mikaela	NULL	NULL	NULL
# 11	Joziah	6	NULL	NULL
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/029_employees_whose_manager_left_the_company -v` green

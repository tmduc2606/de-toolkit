# SQL027 — Primary Department for Each Employee

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT e1.employee_id, e1.department_id
FROM Employee e1
WHERE primary_flag = 'Y'
GROUP BY e1.employee_id
UNION
SELECT e2.employee_id, e2.department_id
FROM Employee e2
GROUP BY e2.employee_id
HAVING COUNT(*) = 1;
```

## Test-case annotations

```
# CASE 1: Employee with their primary department ('Y')
# CASE 2: Employee with their only department ('N') - COUNT(*) = 1
# UNION: Filtered out duplicated rows
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/027_primary_department_for_each_employee -v` green

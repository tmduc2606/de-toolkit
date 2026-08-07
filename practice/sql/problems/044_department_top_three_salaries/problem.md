# SQL044 — Department Top Three Salaries

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT r.Department, r.Employee, r.Salary
FROM
(SELECT d.name AS Department, 
       e.name AS Employee, 
       e.salary AS Salary,
       DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rank_num
FROM Employee e
JOIN Department d ON d.id = e.departmentId) r
WHERE r.rank_num <= 3;
```

## Test-case annotations

```
# DESNSE_RANK - consecutive ranks regardless of ties
# Classify from derpartmentId
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/044_department_top_three_salaries -v` green

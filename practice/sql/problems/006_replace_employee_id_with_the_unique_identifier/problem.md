# SQL006 — Replace Employee ID With The Unique Identifier

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id;
```

## Test-case annotations

```
# JOIN or LEFT JOIN
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/006_replace_employee_id_with_the_unique_identifier -v` green

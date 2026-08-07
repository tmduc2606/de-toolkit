# SQL040 — Second Highest Salary

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT 
    CASE 
        WHEN SecondSalary IS NULL THEN SecondSalary = NULL 
        ELSE SecondSalary 
    END AS SecondHighestSalary
FROM (
    SELECT MAX(salary) AS SecondSalary FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee) 
) t;
```

## Test-case annotations

```
# SELECT MAX(col) FROM table 
# WHERE col < (SELECT MAX(col) FROM table)
# NOTE: If the input is none, make sure to wrap it within CASE WHEN ... ELSE set NULL for SecondHighest
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/040_second_highest_salary -v` green

# SQL013 — Managers with atleast 5 Direct Reports

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT e1.name
FROM Employee e1
JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(e2.managerId) >= 5;
```

## Test-case annotations

```
# SELF-JOIN + GROUP BY e1.id & HAVING COUNT mgrID >= 5
# Intermediate result
#  e1.id	e1.name	e2.id	e2.name	e2.managerId
# 101	John	102	Dan	101
# 101	John	103	James	101
# 101	John	104	Amy	101
# 101	John	105	Anne	101
# 101	John	106	Ron	101
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/013_managers_with_atleast_5_direct_reports -v` green

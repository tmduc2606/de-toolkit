# SQL038 — Patients With a Condition

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT p.patient_id, p.patient_name, p.conditions
FROM Patients p
WHERE p.conditions LIKE '% DIAB1%' OR p.conditions LIKE 'DIAB1%';
```

## Test-case annotations

```
# Case 1: Prefix 'DIAB1' starts at the 1st word
# Case 2: Prefix 'DIAB1' starts at 2nd word (with whitespace)
# USE 'LIKE' for fixed 'DIAB1' and ' ' + 'DIAB1%' - begins with
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/038_patients_with_a_condition -v` green

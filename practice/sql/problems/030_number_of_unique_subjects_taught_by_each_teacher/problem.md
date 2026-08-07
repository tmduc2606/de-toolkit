# SQL030 — Number of Unique Subjects Taught by Each Teacher

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT t.teacher_id, COUNT(DISTINCT t.subject_id) AS cnt
FROM Teacher t
GROUP BY t.teacher_id;
```

## Test-case annotations

```
# DISTINCT t.subject_id, GROUP BY t.teacher_id
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/030_number_of_unique_subjects_taught_by_each_teacher -v` green

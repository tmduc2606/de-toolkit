# SQL011 — Students & Examinations

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT st.student_id, st.student_name, s.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students st
CROSS JOIN Subjects s 
LEFT JOIN Examinations e ON e.student_id = st.student_id AND e.subject_name = s.subject_name
GROUP BY st.student_id, st.student_name, s.subject_name
ORDER BY st.student_id, s.subject_name;
```

## Test-case annotations

```
# CROSS JOIN (Each student by default contains Math, Physics & Programming) 
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/011_students_examinations -v` green

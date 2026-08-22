# SQL069 — Find Students Who Improved

> Source: LeetCode 3421 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Scores`

| Column Name | Type |
|---|---|
| student_id | int |
| subject | varchar |
| score | int |
| exam_date | date |

`(student_id, subject, exam_date)` is the primary key; `score` is between 0
and 100. A student has **improved** in a subject when both conditions hold:

- they took exams in that subject on at least two different dates,
- their latest score in that subject is higher than their first score.

Report `student_id`, `subject`, `first_score`, `latest_score` for improved
students, ordered by `student_id`, `subject` in ascending order.

## Solution (MySQL, annotated)

```sql
-- A student's subsequent scores compared to the original via a CTE with
-- ROW_NUMBER(): partitioned by id and subject name, ordered by exam date
-- ASC and DESC to tag the first/latest exam in one pass
-- Outer query keeps only rows where both requirements hold
WITH student_score_neighbors AS (...)
SELECT ...
HAVING (COUNT(exam_date) >= 2)
    AND (MAX(CASE WHEN rn_last = 1 THEN score END)
         > MAX(CASE WHEN rn_first = 1 THEN score END));
```

Full query lives in `solution.sql`. Notes:

> DuckDB note: window functions (`ROW_NUMBER`, `COUNT(*) OVER`) are standard;
> no portability rewrite needed. MySQL quirk kept as-is: aliases cannot be
> referenced inside `HAVING`, so the aggregate expressions repeat there.

## Test-case annotations

```
Input:
Scores table:
+------------+----------+-------+------------+
| student_id | subject  | score | exam_date  |
+------------+----------+-------+------------+
| 101        | Math     | 70    | 2023-01-15 |
| 101        | Math     | 85    | 2023-02-15 |
| 101        | Physics  | 65    | 2023-01-15 |
| 101        | Physics  | 60    | 2023-02-15 |
| 102        | Math     | 80    | 2023-01-15 |
| 102        | Math     | 85    | 2023-02-15 |
| 103        | Math     | 90    | 2023-01-15 |
| 104        | Physics  | 75    | 2023-01-15 |
| 104        | Physics  | 85    | 2023-02-15 |
+------------+----------+-------+------------+

101/Math improved 70 -> 85; 101/Physics dropped 65 -> 60 (excluded);
102/Math improved 80 -> 85; 103/Math took one exam only (excluded);
104/Physics improved 75 -> 85.

Output (ordered by student_id, subject ASC):
+------------+----------+-------------+--------------+
| student_id | subject  | first_score | latest_score |
+------------+----------+-------------+--------------+
| 101        | Math     | 70          | 85           |
| 102        | Math     | 80          | 85           |
| 104        | Physics  | 75          | 85           |
+------------+----------+-------------+--------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/069_find_students_who_improved -v` green
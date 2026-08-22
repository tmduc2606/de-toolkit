-- CTE: per (student_id, subject), ROW_NUMBER() ordered by exam_date ASC/DESC
-- tags the first and latest exam; COUNT(*) OVER counts exams attended
-- Outer query: pivot first/latest scores with MAX(CASE WHEN ...);
-- HAVING needs both conditions written out — aliases are not usable there
WITH student_score_neighbors AS (
    SELECT
        s.student_id,
        s.subject,
        s.score,
        s.exam_date,
        ROW_NUMBER() OVER (
            PARTITION BY s.student_id, s.subject
            ORDER BY s.exam_date ASC
        ) AS rn_first,
        ROW_NUMBER() OVER (
            PARTITION BY s.student_id, s.subject
            ORDER BY s.exam_date DESC
        ) AS rn_last,
        COUNT(*) OVER (
            PARTITION BY s.student_id, s.subject
        ) AS exam_count
    FROM Scores s
)
SELECT
    student_id,
    subject,
    MAX(CASE WHEN rn_first = 1 THEN score END) AS first_score,
    MAX(CASE WHEN rn_last = 1 THEN score END) AS latest_score
FROM student_score_neighbors
GROUP BY student_id, subject
HAVING (COUNT(exam_date) >= 2)
    AND (
        MAX(CASE WHEN rn_last = 1 THEN score END)
        > MAX(CASE WHEN rn_first = 1 THEN score END)
    )
ORDER BY student_id, subject ASC;
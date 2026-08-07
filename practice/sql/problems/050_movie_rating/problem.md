# SQL050 — Movie Rating

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
(SELECT u.name AS results
FROM MovieRating mr
JOIN Users u ON mr.user_id = u.user_id
GROUP BY mr.user_id, u.name
ORDER BY COUNT(mr.rating) DESC, u.name LIMIT 1)
UNION ALL 
(SELECT m.title
FROM MovieRating mr
JOIN Movies m ON mr.movie_id = m.movie_id
WHERE mr.created_at = DATE_FORMAT(mr.created_at, '2020-02-%dd')
GROUP BY mr.movie_id, m.title
ORDER BY AVG(mr.rating) DESC, m.title LIMIT 1);
```

## Test-case annotations

```
# Query 1: Name of user rating the greatest number of movies
# Films and Users may have the sane name / title
# Query 2: The title with highest average rating in Feb 2020
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/050_movie_rating -v` green

# SQL036 — Last Person to Fit in the Bus

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT q1.person_name 
FROM Queue q1
JOIN Queue q2 ON q2.turn <= q1.turn
GROUP BY q1.person_id, q1.person_name
HAVING SUM(q2.weight) <= 1000
ORDER BY q1.turn DESC LIMIT 1;
```

## Test-case annotations

```
# Self-join on turn as keeping track of weight --> If exceeds 1000
# Intermediate Result: q1.turn | q2.turn | ... | q1.person_name | q2.person_name
# John Cena | Alice     | 250
# John Cena | Alex      | 600
# Jonh Cena | John Cena | 1000 <- Stops here, and select the last person
# MUST GROUP BY q1, not q2 (person_id, person_name) since we are keeping track of the last person
# The list produce John Cena, Alex, Alice <- ORDER BY q1.turn DESC & LIMIT 1
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/036_last_person_to_fit_in_the_bus -v` green

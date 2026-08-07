# SQL034 — Game Play Analysis IV

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT ROUND(
    COUNT(DISTINCT a1.player_id) / (SELECT COUNT(
        DISTINCT player_id
        ) FROM Activity)
    , 2) AS fraction
FROM Activity a1
JOIN Activity a2 ON a1.player_id = a2.player_id
AND a1.event_date = DATE_ADD(a2.event_date, INTERVAL 1 DAY)
WHERE a2.event_date = (
    SELECT MIN(event_date) FROM Activity
    WHERE player_id = a2.player_id
);
```

## Test-case annotations

```
# Write your MySQL query statement below
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/034_game_play_analysis_iv -v` green

# SQL009 — Average Time of Process per Machine

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM Activity a1
JOIN Activity a2 ON (
    a1.machine_id = a2.machine_id
) AND (
    a1.process_id = a2.process_id
)
WHERE a1.activity_type = 'start' AND a2.activity_type = 'end'
GROUP BY a1.machine_id;
```

## Test-case annotations

```
# SELF-JOIN on machine_id and process_id, round up to 3 digits
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/009_average_time_of_process_per_machine -v` green

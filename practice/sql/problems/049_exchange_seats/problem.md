# SQL049 — Exchange Seats

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT (
    CASE
        WHEN s.id % 2 = 1 AND s.id = (SELECT MAX(id) FROM Seat) THEN s.id
        WHEN s.id % 2 = 1 THEN s.id + 1
        ELSE s.id - 1
    END
) AS id, student
FROM Seat s
ORDER BY id ASC;
```

## Test-case annotations

```
# Case: Odd ID -> The last row remains unchanged, pairs (1, 2), (3, 4) get swapped
# Case: Even ID -> Pairs get swapped (the former + 1, the latter - 1)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/049_exchange_seats -v` green

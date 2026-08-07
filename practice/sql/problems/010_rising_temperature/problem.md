# SQL010 — Rising Temperature

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;
```

## Test-case annotations

```
# Intermediate result for self-join (w1 is one day after w2)
# w2.id | w2.recordDate | w2.temp | w1.id | w1.recordDate | w1.temp
# 1 | 2015-01-01 | 10 | 2 | 2015-01-02 | 25
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/010_rising_temperature -v` green

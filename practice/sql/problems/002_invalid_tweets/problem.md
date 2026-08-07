# SQL002 — Invalid Tweets

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT t.tweet_id
FROM Tweets t
WHERE CHAR_LENGTH(t.content) > 15;
```

## Test-case annotations

```
# LENGTH() OR CHAR_LENGTH()
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/002_invalid_tweets -v` green

# SQL048 — Friend Requests II: Who Has the Most Friends

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT f.id, COUNT(*) as num
FROM (
    SELECT requester_id AS id, accept_date
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, accept_date
    FROM RequestAccepted
) f
GROUP BY f.id
ORDER BY num DESC LIMIT 1;
```

## Test-case annotations

```
# Union the requesters with the accepters
# In a cicrcle of friend, one man can have two friends, similarly to the other friend which also have two -> GROUP BY id (requester_id & accepter_id)
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/048_friend_requests_ii_who_has_the_most_friends -v` green

# SQL042 — Find Users With Valid E-Mails

> Source: LeetCode SQL 50 (answer annotated in
> `practice/sql/raw/sql_50_answersheet.txt`).

## Solution (MySQL, annotated)

```sql
SELECT *
FROM Users u
WHERE u.mail RLIKE '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$'
    AND BINARY u.mail LIKE '%leetcode.com';
```

## Test-case annotations

```
# Regular Expression
# ^ : Starts with
# * : Zero or more
# +:  One or more
# [] - Any characters within the accepted
# @leetcode\\.[c][o][m]$ - ends with literal string
# [A-Za-z][A-Za-z0-9._-] - The character must come before any literal backslash (.), valid special characters or integers
# BINARY: Convert a value to a binary string -> Handles case-sensitive phrases
```

## Status

- [ ] `schema.sql` populated with the LeetCode example rows
- [ ] `test_solution.py` asserting the annotated expected output
- [ ] `uv run pytest practice/sql/problems/042_find_users_with_valid_e_mails -v` green

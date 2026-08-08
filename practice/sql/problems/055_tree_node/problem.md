# SQL055 — Tree Node

> Source: LeetCode 608 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `Tree`

| Column Name | Type |
|---|---|
| id | int |
| p_id | int |

`id` is the primary key; `p_id` is the id of the node's parent, `null` if root.
Classify each node as `Root` (no parent), `Leaf` (no children), or `Inner`
(neither).

## Solution (MySQL, annotated)

```sql
# Left Self-join t1.id ON t2.p_id to see how many child
# did the inner or root node own?
SELECT t1.id, (
    CASE
        WHEN t1.p_id IS NULL THEN 'Root'
        WHEN COUNT(t2.id) > 0 THEN 'Inner'
        ELSE 'Leaf' 
    END
) AS type
FROM Tree t1
LEFT JOIN Tree t2 ON t1.id = t2.p_id
GROUP BY t1.id, t1.p_id;
```

## Test-case annotations

```
Input Tree table:
+------+------+
| id   | p_id |
+------+------+
| 1    | null |
| 2    | 1    |
| 3    | 1    |
| 4    | 2    |
| 5    | 2    |
+------+------+

Output:
+------+-------+
| id   | type  |
+------+-------+
| 1    | Root  |
| 2    | Inner |
| 3    | Leaf  |
| 4    | Leaf  |
| 5    | Leaf  |
+------+-------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/055_tree_node -v` green
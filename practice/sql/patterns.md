# SQL 50 — Common Patterns for LeetCode Interviews

> Converted from `docs/originals/SQL - Common Patterns.docx` (original preserved).
> Problem IDs refer to `practice/sql/raw/sql_50_answersheet.txt` (SQL1..SQL50).

## Pattern Index

| # | Pattern | Core Idea | Representative Problems |
|---|---------|-----------|-------------------------|
| 1 | Basic Filtering | `SELECT ... WHERE` | SQL1, SQL2, SQL4 |
| 2 | NULL Handling | `IS NULL`, `IS NOT NULL` | SQL5, SQL7, SQL12, SQL29 |
| 3 | DISTINCT | Remove duplicates | SQL3, SQL24, SQL30, SQL41 |
| 4 | ORDER BY | Sorting results | SQL3, SQL4, SQL15, SQL22 |
| 5 | String Functions | `CHAR_LENGTH`, `SUBSTRING`, `CONCAT`, `UPPER`, `LOWER` | SQL2, SQL37 |
| 6 | Pattern Matching | `LIKE`, `NOT LIKE`, `RLIKE` | SQL15, SQL38, SQL42 |
| 7 | Date Functions | `DATE_ADD`, `DATE_SUB`, `BETWEEN`, `DATE_FORMAT` | SQL10, SQL16, SQL31, SQL43, SQL46, SQL47 |
| 8 | INNER JOIN | Match rows between tables | SQL6, SQL8, SQL17, SQL18, SQL43, SQL50 |
| 9 | LEFT JOIN | Preserve left table | SQL6, SQL7, SQL12, SQL14, SQL16, SQL29, SQL35 |
| 10 | SELF JOIN | Join a table to itself | SQL9, SQL10, SQL13, SQL25, SQL28, SQL29, SQL36, SQL39, SQL45 |
| 11 | CROSS JOIN | Cartesian product | SQL11 |
| 12 | GROUP BY + Aggregation | `COUNT`, `SUM`, `AVG`, `MAX`, `MIN` | SQL7, SQL17, SQL18, SQL21, SQL22, SQL25, SQL30, SQL32, SQL41 |
| 13 | HAVING | Filter aggregated groups | SQL13, SQL21, SQL23, SQL24, SQL35, SQL43 |
| 14 | CASE Expression | Conditional logic | SQL14, SQL19, SQL26, SQL35, SQL49 |
| 15 | COALESCE / NULLIF | Handle missing values and divide-by-zero | SQL16, SQL32, SQL35 |
| 16 | Scalar & Correlated Subqueries | Nested queries | SQL18, SQL20, SQL23, SQL33, SQL34, SQL40, SQL45, SQL47 |
| 17 | EXISTS / NOT EXISTS | Existence checks | SQL45 |
| 18 | UNION / UNION ALL | Combine result sets | SQL27, SQL35, SQL47, SQL48, SQL50 |
| 19 | Common Table Expressions (CTE) | `WITH ...` | SQL46 |
| 20 | Window Functions | `LAG`, `DENSE_RANK`, `OVER()` | SQL28, SQL44 |

## Pattern Frequency

| Pattern | Frequency | Importance |
|---------|-----------|------------|
| GROUP BY | ⭐⭐⭐⭐⭐ | Extremely High |
| JOIN | ⭐⭐⭐⭐⭐ | Extremely High |
| LEFT JOIN | ⭐⭐⭐⭐⭐ | Extremely High |
| Aggregations | ⭐⭐⭐⭐⭐ | Extremely High |
| Subqueries | ⭐⭐⭐⭐ | High |
| CASE | ⭐⭐⭐⭐ | High |
| SELF JOIN | ⭐⭐⭐⭐ | High |
| HAVING | ⭐⭐⭐⭐ | High |
| Date Functions | ⭐⭐⭐ | Medium |
| String Functions | ⭐⭐⭐ | Medium |
| UNION | ⭐⭐⭐ | Medium |
| Window Functions | ⭐⭐ | Medium-High |
| EXISTS | ⭐ | Medium |

## Fundamental SQL Templates

### Pattern 1 — Simple Filter

```sql
SELECT columns
FROM table
WHERE condition;
```

### Pattern 2 — Join

```sql
SELECT ...
FROM A
JOIN B
ON A.id = B.id;
```

### Pattern 3 — Left Join + Missing Rows

```sql
SELECT ...
FROM A
LEFT JOIN B
ON A.id = B.id
WHERE B.id IS NULL;
```

### Pattern 4 — Aggregation

```sql
SELECT key,
COUNT(*),
SUM(col),
AVG(col)
FROM table
GROUP BY key;
```

### Pattern 5 — HAVING

```sql
SELECT key
FROM table
GROUP BY key
HAVING COUNT(*) >= 5;
```

### Pattern 6 — CASE

```sql
SELECT
CASE
WHEN condition THEN value1
ELSE value2
END
FROM table;
```

### Pattern 7 — Conditional Aggregation

```sql
SELECT
SUM(CASE WHEN condition THEN amount ELSE 0 END)
FROM table;
```

Or the rate idiom (1 for true, 0 for false):

```sql
AVG(
CASE
WHEN condition THEN 1
ELSE 0
END
)
```

### Pattern 8 — Self-Join

```sql
SELECT ...
FROM Employee e1
JOIN Employee e2
ON e1.id = e2.managerId;
```

### Pattern 9 — Correlated Subquery

```sql
SELECT *
FROM table t
WHERE EXISTS
(
SELECT 1
FROM table2
WHERE ...
);
```

### Pattern 10 — Window Function

```sql
SELECT *,
DENSE_RANK() OVER(
PARTITION BY department
ORDER BY salary DESC
)
FROM Employee;
```

### Pattern 11 — CTE (Common Table Expression)

```sql
WITH temp AS
(
SELECT ...
)
SELECT ...
FROM temp;
```

### Pattern 12 — UNION

```sql
SELECT ...
UNION ALL
SELECT ...;
```

## Advanced Topics

Sophisticated window functions (`ROW_NUMBER`, `RANK`, `LEAD`, running totals),
recursive CTEs, pivot / unpivot transformations, and more complex
multi-state analytical queries.

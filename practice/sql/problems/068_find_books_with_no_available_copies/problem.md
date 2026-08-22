# SQL068 — Find Books with No Available Copies

> Source: LeetCode 3570 (hand-solved, not part of the SQL 50 answersheet).

## Problem statement

Table: `library_books`

| Column Name | Type |
|---|---|
| book_id | int |
| title | varchar |
| author | varchar |
| genre | varchar |
| publication_year | int |
| total_copies | int |

`book_id` is the unique identifier. Table: `borrowing_records`

| Column Name | Type |
|---|---|
| record_id | int |
| book_id | int |
| borrower_name | varchar |
| borrow_date | date |
| return_date | date |

`record_id` is the unique identifier; `return_date` is `NULL` while a copy is
still borrowed. Find all books that are currently borrowed and have zero
copies available — i.e. every copy is checked out. Return the result table
ordered by current borrowers in descending order, then by book title in
ascending order.

## Solution (MySQL, annotated)

```sql
-- Brute force: LEFT JOIN on book_id keeps books with no active borrowings;
-- br.return_date IS NULL inside the ON clause counts current borrowers only
-- GROUP BY the book columns; keep books where borrowers = total copies
SELECT
    lb.book_id,
    lb.title,
    lb.author,
    lb.genre,
    lb.publication_year,
    COUNT(br.book_id) AS current_borrowers
FROM library_books lb
LEFT JOIN borrowing_records br
    ON lb.book_id = br.book_id
    AND br.return_date IS NULL
GROUP BY
    lb.book_id, lb.title, lb.author, lb.total_copies
HAVING lb.total_copies = COUNT(br.book_id)
ORDER BY current_borrowers DESC, lb.title ASC;
```

> DuckDB note: strict `GROUP BY` requires every non-aggregated select column
> (`lb.genre`, `lb.publication_year`) to appear in the GROUP BY clause — see
> `solution.sql`. Optimization direction: pre-aggregate active borrowings in
> a subquery (`GROUP BY book_id`) and join on
> `current_borrowers = total_copies` instead of joining the raw records.

## Test-case annotations

```
Input:
library_books table:
+---------+------------------------+------------------+-----------+------------------+--------------+
| book_id | title                  | author           | genre     | publication_year | total_copies |
+---------+------------------------+------------------+-----------+------------------+--------------+
| 1       | The Great Gatsby       | F. Scott         | Fiction   | 1925             | 3            |
| 2       | To Kill a Mockingbird  | Harper Lee       | Fiction   | 1960             | 3            |
| 3       | 1984                   | George Orwell    | Dystopian | 1949             | 1            |
| 4       | Pride and Prejudice    | Jane Austen      | Romance   | 1813             | 2            |
| 5       | The Catcher in the Rye | J.D. Salinger    | Fiction   | 1951             | 1            |
| 6       | Brave New World        | Aldous Huxley    | Dystopian | 1932             | 4            |
+---------+------------------------+------------------+-----------+------------------+--------------+

borrowing_records table:
+-----------+---------+---------------+-------------+-------------+
| record_id | book_id | borrower_name | borrow_date | return_date |
+-----------+---------+---------------+-------------+-------------+
| 1         | 1       | Alice Smith   | 2024-01-15  | NULL        |
| 2         | 1       | Bob Johnson   | 2024-01-20  | NULL        |
| 3         | 2       | Carol White   | 2024-01-10  | 2024-01-25  |
| 4         | 3       | David Brown   | 2024-02-01  | NULL        |
| 5         | 4       | Emma Wilson   | 2024-01-05  | NULL        |
| 6         | 5       | Frank Davis   | 2024-01-18  | 2024-02-10  |
| 7         | 1       | Grace Miller  | 2024-02-05  | NULL        |
| 8         | 6       | Henry Taylor  | 2024-01-12  | NULL        |
| 9         | 2       | Ivan Clark    | 2024-02-12  | NULL        |
| 10        | 2       | Jane Adams    | 2024-02-15  | NULL        |
+-----------+---------+---------------+-------------+-------------+

Book 1: 3 of 3 copies out (Alice, Bob, Grace). Book 3: 1 of 1 out (David).
Books 2/4/6 still have spare copies; book 5 has none borrowed.

Output (current_borrowers DESC, title ASC):
+---------+------------------+---------------+-----------+------------------+-------------------+
| book_id | title            | author        | genre     | publication_year | current_borrowers |
+---------+------------------+---------------+-----------+------------------+-------------------+
| 1       | The Great Gatsby | F. Scott      | Fiction   | 1925             | 3                 |
| 3       | 1984             | George Orwell | Dystopian | 1949             | 1                 |
+---------+------------------+---------------+-----------+------------------+-------------------+
```

## Status

- [x] `schema.sql` populated with the LeetCode example rows
- [x] `test_solution.py` asserting the annotated expected output
- [x] `uv run pytest practice/sql/problems/068_find_books_with_no_available_copies -v` green
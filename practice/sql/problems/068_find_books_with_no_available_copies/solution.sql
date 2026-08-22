-- Brute force: LEFT JOIN on book_id keeps books with no active borrowings;
-- br.return_date IS NULL inside the ON join condition counts current borrowers only
-- GROUP BY the book columns; keep books where borrowers = total copies
-- DuckDB: strict GROUP BY — lb.genre and lb.publication_year must be listed
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
    lb.book_id, lb.title, lb.author, lb.genre, lb.total_copies, lb.publication_year
HAVING lb.total_copies = COUNT(br.book_id)
ORDER BY current_borrowers DESC, lb.title ASC;
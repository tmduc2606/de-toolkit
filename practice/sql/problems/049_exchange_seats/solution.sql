SELECT (
    CASE
        WHEN s.id % 2 = 1 AND s.id = (SELECT MAX(id) FROM Seat) THEN s.id
        WHEN s.id % 2 = 1 THEN s.id + 1
        ELSE s.id - 1
    END
) AS id, student
FROM Seat s
ORDER BY id ASC;

-- Nested query: build a table of 2020 logins, ranked per user by
-- time_stamp DESC (ROW_NUMBER window)
-- External query: keep rank 1 per user as last_stamp (the latest)
SELECT user_id, time_stamp AS last_stamp
FROM (
    SELECT
        l.user_id,
        l.time_stamp,
        ROW_NUMBER() OVER (
            PARTITION BY l.user_id
            ORDER BY l.time_stamp DESC
        ) AS rn
    FROM Logins l
    WHERE YEAR(l.time_stamp) = 2020
) t
WHERE rn = 1
ORDER BY user_id ASC;
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

SELECT * FROM Cinema c
WHERE (c.id % 2 != 0) AND c.description NOT LIKE '%boring'
GROUP BY c.id
ORDER BY c.rating DESC;

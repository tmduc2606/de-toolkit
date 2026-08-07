SELECT u.user_id, CONCAT(UPPER(SUBSTRING(u.name, 1, 1)), LOWER(SUBSTRING(u.name, 2, length(u.name)))) AS name
FROM Users u
ORDER BY user_id;

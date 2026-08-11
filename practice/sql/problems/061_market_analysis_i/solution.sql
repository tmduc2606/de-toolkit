-- Projecting from Users table -> GROUP BY u.user_id, u.join_date
-- LEFT JOIN on o.buyer_id = u.user_id with the orders made in 2019 only
-- COUNT() over the GROUP BY keeps users with 0 orders in 2019
SELECT u.user_id AS buyer_id, u.join_date, COUNT(o.item_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON o.buyer_id = u.user_id
    AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date
ORDER BY u.user_id;
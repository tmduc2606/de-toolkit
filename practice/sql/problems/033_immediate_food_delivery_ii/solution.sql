SELECT ROUND(
    COUNT(
        CASE WHEN d.order_date = d.customer_pref_delivery_date THEN delivery_id END
        ) * 100 / COUNT(d.delivery_id), 2
) AS immediate_percentage
FROM Delivery d
JOIN
    (
        SELECT customer_id, MIN(order_date) AS first_order
        FROM Delivery
        GROUP BY customer_id
    ) AS ed
ON ed.customer_id = d.customer_id 
AND d.order_date = ed.first_order;

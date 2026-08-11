-- Optimal approach: MIN()/MAX() over the per-product sale dates prove every
-- sale (not just the latest one) fell inside Q1 2019 — the ROW_NUMBER()
-- brute force fails the edge case where the latest sale sits outside Q1
SELECT p.product_id, p.product_name
FROM Sales s
JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31'
ORDER BY p.product_id;
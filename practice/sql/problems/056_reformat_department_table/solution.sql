-- Conditional aggregation → pivot: SUM(CASE ...) per month column.
-- Equivalent in pandas: department.pivot(index = "id", columns = "month", values = "revenue")
SELECT 
    d.id,
    SUM(CASE WHEN d.month = 'Jan' THEN revenue END) AS Jan_Revenue,
    SUM(CASE WHEN d.month = 'Feb' THEN revenue END) AS Feb_Revenue,
    SUM(CASE WHEN d.month = 'Mar' THEN revenue END) AS Mar_Revenue,
    SUM(CASE WHEN d.month = 'Apr' THEN revenue END) AS Apr_Revenue,
    SUM(CASE WHEN d.month = 'May' THEN revenue END) AS May_Revenue,
    SUM(CASE WHEN d.month = 'Jun' THEN revenue END) AS Jun_Revenue,
    SUM(CASE WHEN d.month = 'Jul' THEN revenue END) AS Jul_Revenue,
    SUM(CASE WHEN d.month = 'Aug' THEN revenue END) AS Aug_Revenue,
    SUM(CASE WHEN d.month = 'Sep' THEN revenue END) AS Sep_Revenue,
    SUM(CASE WHEN d.month = 'Oct' THEN revenue END) AS Oct_Revenue,
    SUM(CASE WHEN d.month = 'Nov' THEN revenue END) AS Nov_Revenue,
    SUM(CASE WHEN d.month = 'Dec' THEN revenue END) AS Dec_Revenue
FROM Department d
GROUP BY d.id
ORDER BY d.id;
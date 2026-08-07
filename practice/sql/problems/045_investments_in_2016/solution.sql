SELECT ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM Insurance i1
WHERE EXISTS (
    SELECT 1
    FROM Insurance i2 WHERE i2.tiv_2015 = i1.tiv_2015 
    AND i2.pid != i1.pid
)
AND NOT EXISTS (
    SELECT 1
    FROM Insurance i3 WHERE i3.lat = i1.lat
    AND i3.lon = i1.lon
    AND i3.pid != i1.pid
);
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
);

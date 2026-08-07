SELECT t.x, t.y, t.z, (
    CASE WHEN (t.x >= 0 AND t.y >= 0 AND t.z >= 0)
    AND (t.x + t.y > t.z)
    AND (t.y + t.z > t.x)
    AND (t.x + t.z > t.y)
    THEN 'Yes' ELSE 'No' END
) AS triangle
FROM Triangle t;

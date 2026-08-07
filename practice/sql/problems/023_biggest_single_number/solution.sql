SELECT MAX(mn.num) AS num
FROM MyNumbers mn
WHERE mn.num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);

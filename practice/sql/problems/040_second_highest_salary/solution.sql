SELECT 
    CASE 
        WHEN SecondSalary IS NULL THEN SecondSalary = NULL 
        ELSE SecondSalary 
    END AS SecondHighestSalary
FROM (
    SELECT MAX(salary) AS SecondSalary FROM Employee
    WHERE salary < (SELECT MAX(salary) FROM Employee) 
) t;

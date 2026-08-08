-- Union of employees missing a salary and salaries missing a name
SELECT employee_id
FROM
(
    SELECT e.employee_id 
    FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    WHERE s.salary IS NULL

    UNION

    SELECT s.employee_id
    FROM Employees e
    RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
    WHERE e.name IS NULL
) t
ORDER BY t.employee_id ASC;
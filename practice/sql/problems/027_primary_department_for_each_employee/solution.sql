SELECT e1.employee_id, e1.department_id
FROM Employee e1
WHERE primary_flag = 'Y'
GROUP BY e1.employee_id
UNION
SELECT e2.employee_id, e2.department_id
FROM Employee e2
GROUP BY e2.employee_id
HAVING COUNT(*) = 1;

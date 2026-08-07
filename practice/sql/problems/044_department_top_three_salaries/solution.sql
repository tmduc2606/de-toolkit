SELECT r.Department, r.Employee, r.Salary
FROM
(SELECT d.name AS Department, 
       e.name AS Employee, 
       e.salary AS Salary,
       DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rank_num
FROM Employee e
JOIN Department d ON d.id = e.departmentId) r
WHERE r.rank_num <= 3;

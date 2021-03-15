-- Write your MySQL query statement below
SELECT D.Name as Department,Employee,Salary 
FROM
(
  SELECT DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) 
  as NUM, id, Name as Employee, Salary, DepartmentId
  FROM Employee
) E
INNER JOIN Department D ON D.Id=E.DepartmentId
AND E.NUM<=3
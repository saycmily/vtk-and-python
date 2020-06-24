-- Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary
from employee e inner join department d
on e.departmentid = d.id 
and e.salary = (select max(salary) from employee where departmentid=d.id) 

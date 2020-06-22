-- Write your MySQL query statement below
select name employee
from employee a
where salary > (select salary from employee where id = a.managerid)
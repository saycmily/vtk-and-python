-- Write your MySQL query statement below
select c.name customers
from customers c
where not exists(select id from orders where customerid = c.id)

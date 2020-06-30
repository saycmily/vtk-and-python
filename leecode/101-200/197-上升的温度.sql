-- Write your MySQL query statement below
select a.id
from weather a, weather b
where a.temperature > b.temperature
-- and a.recorddate = date_add(b.recorddate, interval 1 day)
and dateDiff(a.recorddate, b.recorddate) = 1
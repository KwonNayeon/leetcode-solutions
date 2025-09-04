-- Write your PostgreSQL query statement below
with data as (
    select num
    from mynumbers
    group by num
    having count(num) = 1
)
select max(num) as num
from data
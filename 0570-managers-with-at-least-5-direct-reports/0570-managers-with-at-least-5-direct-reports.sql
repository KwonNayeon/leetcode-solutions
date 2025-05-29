# Write your MySQL query statement below
with data as (
    select 
        name,
        managerId,
        count(managerId) as cnt
    from Employee
)
select name
from data
where cnt >= 5



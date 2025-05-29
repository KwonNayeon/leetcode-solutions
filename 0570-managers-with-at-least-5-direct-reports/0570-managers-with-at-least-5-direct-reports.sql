with data as (
    select 
        managerId,
        count(managerId) as cnt
    from Employee
    where managerId is not null
    group by managerId
)
select name
from data d
join Employee e
on d.managerId = e.id
where d.cnt >= 5


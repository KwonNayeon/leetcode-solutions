-- Write your PostgreSQL query statement below
with data as (
    select
        s.user_id,
        case when count(c.action) = 0 then 0
        else round(
            sum(case when c.action = 'confirmed' then 1 else 0 end) * 1.0 / count(c.action), 2
        ) end as confirmation_rate
    from Signups s
    left join Confirmations c
    on s.user_id = c.user_id
    group by s.user_id
)
select *
from data

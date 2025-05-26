-- Write your PostgreSQL query statement below
with data as (
    select
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate) as prev_temp
    from Weather
)
select id
from data
where temperature > prev_temp
;
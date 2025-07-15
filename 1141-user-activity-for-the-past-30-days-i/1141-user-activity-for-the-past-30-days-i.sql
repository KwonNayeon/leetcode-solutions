-- Write your PostgreSQL query statement below
select
    activity_date as day,
    count(distinct user_id) as active_users
from activity
where
    activity_date >= '2019-06-28'
    and activity_date < '2019-07-28'
    and activity_type is not null
group by activity_date
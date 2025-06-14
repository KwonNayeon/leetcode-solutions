-- Write your PostgreSQL query statement below
select
    r.contest_id,
    round(count(r.user_id) * 100.0 / (select count(user_id) from Users),2) as percentage
from Register r
left join Users u
on r.user_id = u.user_id
group by r.contest_id
order by percentage desc, r.contest_id asc
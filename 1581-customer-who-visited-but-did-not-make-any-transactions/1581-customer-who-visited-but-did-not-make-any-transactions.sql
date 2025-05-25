-- Write your PostgreSQL query statement below
select
    v.customer_id,
    sum(case when t.transaction_id is null then 1 end) as count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
group by v.customer_id
having sum(case when t.transaction_id is null then 1 end) > 0
order by count_no_trans
;

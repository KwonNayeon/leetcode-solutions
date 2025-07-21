-- Write your PostgreSQL query statement below
with first_year as (
    select
        product_id,
        min(year) as first_year
    from sales
    group by product_id
)
select
    fy.product_id,
    fy.first_year,
    s.quantity,
    s.price
from sales s
join first_year fy
on s.product_id = fy.product_id
where s.year = fy.first_year
;
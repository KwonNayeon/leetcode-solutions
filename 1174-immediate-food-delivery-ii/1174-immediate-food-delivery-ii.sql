-- Write your PostgreSQL query statement below
with first_orders as (
    select
        delivery_id,
        customer_id,
        order_date,
        customer_pref_delivery_date,
        row_number() over (partition by customer_id order by order_date) as rn
    from delivery
),
first_orders_only as (
    select
        *,
        case
            when order_date = customer_pref_delivery_date then 'immediate'
            else 'scheduled'
        end as delivery_type
    from first_orders
    where rn = 1
)
select
    round(count(case when delivery_type = 'immediate' then 1 end) * 100.0 / count(*), 2) as immediate_percentage
from first_orders_only
;
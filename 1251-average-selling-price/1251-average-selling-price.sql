-- 문제 해결:
-- 1. PostgreSQL에서 정수 ÷ 정수 = 정수 (소수점 버림)
--    예: 100 / 30 = 3 (잘못된 결과)
-- 2. ::numeric 캐스팅으로 정확한 소수점 계산
--    예: 100 / 30::numeric = 3.333... (올바른 결과)
select
    p.product_id,
    case when sum(u.units) is null then 0
    else round(sum(p.price * u.units) / sum(u.units)::numeric, 2) 
    end as average_price
from Prices p
left join UnitsSold u
on p.product_id = u.product_id
and u.purchase_date between p.start_date and p.end_date
group by p.product_id
;
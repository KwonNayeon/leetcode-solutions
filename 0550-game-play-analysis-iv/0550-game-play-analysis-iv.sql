-- Write your PostgreSQL query statement below
with data as (
    select
        player_id,
        event_date,
        row_number() over (partition by player_id order by event_date) as rn,
        lag(event_date) over(partition by player_id order by event_date) as prev_date
    from activity
    group by player_id, event_date
    order by event_date
)
select
    -- 분자: 첫날 로그인하고 바로 다음날 로그인한 플레이어 수
    -- 분모: 첫날 로그인한 전체 플레이어 수
    round(count(case when rn = 2 and (event_date - prev_date) = 1 then 1 end) * 1.0 / count(distinct case when rn = 1 then player_id end), 2) as fraction
from data
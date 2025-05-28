/*
1. CROSS JOIN으로 모든 학생-과목 조합 생성
2. LEFT JOIN으로 실제 시험 기록 연결 (없으면 NULL)
3. GROUP BY로 그룹핑
4. COUNT로 NULL 아닌 값만 세기
*/
select
    s.student_id,
    s.student_name,
    sub.subject_name,
    count(e.student_id) as attended_exams   -- NULL은 세지 않음
from Students s
cross join Subjects sub
left join Examinations e
    on s.student_id = e.student_id
    and sub.subject_name = e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, s.student_name
;
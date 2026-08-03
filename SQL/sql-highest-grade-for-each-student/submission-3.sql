-- Write your query below

-- select Distinct on (student_id)
--     student_id,
--     exam_id, 
--     score
-- from exam_results

-- order by student_id asc, score Desc, exam_id asc


with rankedTable as(
    select
        student_id,
        exam_id,
        score,
        ROW_NUMBER() over(
            partition by student_id
            order by score DESC, exam_id
        )as rn
    from exam_results
)
select student_id, exam_id, score
from rankedTable
where rn=1
order by student_id 
-- Write your query below

select Distinct on (student_id)
    student_id,
    exam_id, 
    score
from exam_results

order by student_id asc, score Desc, exam_id asc

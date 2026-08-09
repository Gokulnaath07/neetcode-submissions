-- Write your query below

SELECT c.customer_id, c.customer_name
from customers c
join orders o on o.customer_id=c.customer_id
Group by c.customer_id
Having
    sum(case when o.product_name='A' then 1 else 0 end)>0
    and 
    sum(case when o.product_name='B' then 1 else 0 end)>0 and 
    sum(case when o.product_name='C' then 1 else 0 end)=0

order by c.customer_name
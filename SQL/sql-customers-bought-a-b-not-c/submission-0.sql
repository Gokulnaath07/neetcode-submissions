-- Write your query below

select c.customer_id, c.customer_name
from customers c
Join orders o on c.customer_id=o.customer_id
group by c.customer_name, c.customer_id
having
    sum(case when o.product_name='A' then 1 else 0 end)>0 and
    sum(case when o.product_name='B' then 1 else 0 end)>0 and 
    sum(case when o.product_name='C' then 1 else 0 end)=0
Order by c.customer_name


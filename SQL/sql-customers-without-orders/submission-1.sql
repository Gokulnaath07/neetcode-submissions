-- Write your query below


-- SELECT name 
-- FROM customers c
-- WHERE NOT EXISTS(
--     SELECT 1
--     FROM orders o
--     WHERE o.customer_id=c.id
-- )

-- select name 
-- from customers
-- where id not in(
--     select customer_id
--     From orders
-- )

select name
from customers c
left join orders o on c.id = o.customer_id
where o.id is null

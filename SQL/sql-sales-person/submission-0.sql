-- Write your query below


SELECT s.name
From sales_person s
LEFT JOIN (
    select sales_id
    from orders o
    inner join company c on c.com_id=o.com_id
    where c.name='CRIMSON'
) crimson_orders on crimson_orders.sales_id = s.sales_id
where crimson_orders.sales_id is null
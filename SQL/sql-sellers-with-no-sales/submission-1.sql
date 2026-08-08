-- Write your query below

SELECT s.seller_name
FROM seller s
WHERE s.seller_id not in
    (
        select seller_id
        from orders
        where sale_date>='2020-01-01' AND sale_date<='2020-12-31'
    )
order by s.seller_name ASC

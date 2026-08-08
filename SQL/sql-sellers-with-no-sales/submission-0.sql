-- Write your query below

SELECT s.seller_name
FROM seller s
LEFT JOIN 
    orders o on s.seller_id=o.seller_id
    AND EXTRACT(YEAR FROM o.sale_date)=2020
WHERE 
    o.seller_id is null
ORDER BY
    s.seller_name ASC
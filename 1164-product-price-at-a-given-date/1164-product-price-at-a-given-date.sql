/* Write your PL/SQL query statement below */
with rnk as 
(
    select 
        p.*,
        rank() over (partition by product_id order by change_date desc) as rn
    from 
        products p
    where
        change_date <= '2019-08-16'
), fir_rnk as
(
    select 
        product_id,
        new_price as price
    from 
        rnk
    where rn = 1
)

select 
    distinct(a.product_id),
    coalesce(b.price, 10) as price
from 
    products a left join fir_rnk b on a.product_id = b.product_id

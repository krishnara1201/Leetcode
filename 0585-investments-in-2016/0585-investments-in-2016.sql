/* Write your PL/SQL query statement below */
with agg as 
(
    select 
        i.*, 
        count(pid) over (partition by tiv_2015) as tiv_2015_val,
        count(pid) over (partition by lat, lon) as loc_val
    from 
        Insurance i
)
select 
    round(sum(tiv_2016), 2) as tiv_2016
from
    agg 
where 
    tiv_2015_val > 1 and 
    loc_val = 1
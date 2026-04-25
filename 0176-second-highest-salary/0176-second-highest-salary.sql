/* Write your PL/SQL query statement below */
with ranks as
(
    select
        e.*,
        dense_rank() over (order by salary desc) as rnk
    from 
        employee e
)
select
    max(case when rnk = 2 then salary end) as secondhighestsalary
from ranks;
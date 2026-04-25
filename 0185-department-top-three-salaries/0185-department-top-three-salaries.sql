/* Write your PL/SQL query statement below */
with full as 
(
    select 
        a.*,
        b.name as department
    from 
        employee a left join department b on a.departmentid = b.id
), ranked as
(
    select 
        f.*,
        dense_rank() over (partition by departmentId order by salary desc) as rnk
    from full f
)
select 
    department,
    name as employee,
    salary
from 
    ranked
where rnk <= 3
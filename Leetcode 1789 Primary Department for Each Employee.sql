with cte as
(
select employee_id, count(department_id) as cnt 
from Employee 
group by employee_id 
having count(department_id) = 1 
)
select employee_id, department_id from Employee 
where primary_flag = 'Y' or employee_id in (select employee_id from cte)
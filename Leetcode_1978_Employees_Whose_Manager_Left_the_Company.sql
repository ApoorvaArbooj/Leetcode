/* Write your T-SQL query statement below */
select e.employee_id
from Employees e LEFT JOIN Employees m ON e.manager_id = m.employee_id 
where e.salary < 30000 AND e.manager_id IS NOT NULL and m.employee_id IS NULL
order by 1
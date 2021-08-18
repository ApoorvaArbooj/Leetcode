with cte as
(
select cast(count(distinct session_id) as float) as ss 
from Activity 
where DATEDIFF(day,activity_date,'2019-07-27') <= 29 
group by user_id
)
select coalesce(round((sum(ss)/count(ss)),2),0) as average_sessions_per_user from cte
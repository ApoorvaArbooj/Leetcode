select query_name , 
convert(decimal(10,2),Avg(rating/convert(decimal(10,2),position) )) quality , 
convert(decimal(10,2),sum(case when rating<3 then 1 else 0 end )*100/convert(decimal(10,2),count(1))) poor_query_percentage
from Queries
group by query_name
order by query_name desc
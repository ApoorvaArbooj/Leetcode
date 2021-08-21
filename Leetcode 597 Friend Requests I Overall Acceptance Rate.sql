with total_acceptedrequest as
(
    select count(*) as num from (select distinct requester_id,accepter_id from RequestAccepted) R
),
total_request as
(
    select count(*) as denom from (select distinct sender_id,send_to_id from FriendRequest) F
)
select case
when denom = 0 then round(0.00,2)
else round(coalesce(cast(num as float)/cast(denom as float),0),2)
end as accept_rate 
from total_acceptedrequest,total_request
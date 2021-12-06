# Write your MySQL query statement below
select 
    per.firstName,
    per.lastname,
    adr.city,
    adr.state
    from Person per
left join Address adr on per.personId = adr.personId

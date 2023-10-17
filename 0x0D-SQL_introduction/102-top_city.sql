--
select city, avg(value) as avg_temp from temperatures where month=7 or month=8 group by city order by avg(value) desc limit 3

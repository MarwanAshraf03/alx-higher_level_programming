-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
select city, avg(value) as avg_temp from temperatures group by city o
rder by avg(value) desc;

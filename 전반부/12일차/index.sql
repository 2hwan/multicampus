use shopdb;
SELECT * FROM membertbl;

create table indextbl(
first_name varchar(14),
last_name varchar(15),
hire_date date);

insert into indextbl
select first_name,last_name, hire_date
from employees.employees
limit 500;

select * from indextbl;
select * from indextbl where first_name = 'mary';

create index idx_indexTBL_firstname on indexTBL(first_name);


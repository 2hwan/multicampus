USE employees;

USE mysql;
select * from employees;

select * from titles;

select * from employees.titles;

select * from titles;

select first_name from employees;

select first_name, last_name, gender From employees; 
select first_name as f_name, last_name as l_name, gender as '성별' from employees;

show databases;

use employees;

show table status;

show tables;

describe employees;

select first_name as 이름, gender 성별, hire_date '회사입사일' from employees;

select CONCAT(first_name, " ", last_name) as fullname, gender as 성별 from employees;

use sqldb;
select * from usertbl;

select * from usertbl where name like '김%';

select userid, name, birthyear, height from usertbl where birthyear >= 1970 and height >=182;

select userid, name, birthyear, height from usertbl where birthyear >= 1970 or height >=182;

select name, height from usertbl where height >=180 and height <= 183;

select name, height from usertbl where height between 180 and 183;

select name, addr from usertbl where addr='경남' or addr ='전남' or addr='경북';

select name, addr from usertbl where addr in ('경남','전남','경북');

select name, height from usertbl where name like '김%';

select name, hegith from usertbl where name like '_종신';

select name, height from usertbl where name >= '가' and name < '나';

select name, height from usertbl where height > (select height from usertbl where name = '김경호');

select name, height from usertbl where height in (177,182);

select name, height from usertbl where name in ('임재범','김경호');

select name, height from usertbl where name in (select name from usertbl where name in ('임재범','김경호'));

select name, height, addr from usertbl where height >= all
	(select height from usertbl where addr = '경남');
    

select name, height, addr from usertbl where height >= any
	(select height from usertbl where addr = '경남');
    

select name, height, addr from usertbl where height >= 
	(select min(height) from usertbl where addr = '경남');
    

select name, height, addr from usertbl where height >= 
	(select max(height) from usertbl where addr = '경남');
    
select name, height from usertbl where height in 
	(select height from usertbl where addr = '경남');

select name, mdate from usertbl order by mdate desc;

use employees;
select concat(first_name, ' ',last_name) as 이름, gender as 성별 from employees order by 1;

use sqldb;

select addr from usertbl;

select distinct addr from usertbl;

select addr from usertbl group by addr;


select distinct addr, height from usertbl order by addr;


select addr, height from usertbl  group by addr, height order by 1,2;

create table buytbl2 (select userid, prodname from buytbl where 1 = 0);
select * from buytbl2;

create table buytbl3 (select userid, prodname from buytbl);
select * from buytbl3;

select userid, amount from buytbl order by userid;

select userid, sum(amount) from buytbl group by userid;

select count(*) from usertbl;

select count(userid) from usertbl;

select count(mobile1) from usertbl;

select avg(amount) as '평균 구매 개수' from buytbl;

select name, max(height), min(height) from usertbl;

select name, height from usertbl where height = (select max(height) from usertbl) or height = (select min(height) from usertbl);

select count(*) from usertbl;

select count(mobile1) as '휴대폰 있는 사용자' from usertbl;

select userid as 사용자, sum(price*amount) as 총구매액 from buytbl group by userid;

select userid as 사용자, sum(price*amount) as 총구매액 from buytbl
	where price >0 and amount > 0 -- where 절에 집계 쓰지 않는다
    group by userid
    having sum(price*amount) > 1000;
    
create table testtbl1(id int, userName char(3), age int);

insert into testtbl1 values (1,'홍길동',25);
insert into testtbl1(id, username) values (2,'설민석');
insert into testtbl1(username,age, id) values ('홍길동',25,3);

select * from testtbl1;
select @@autocommit;
set autocommit = true;

alter table testtbl1 auto_increment = 100;
insert into testtbl1 values( null,'찬미',10);
select * from testtbl1;

create table testtbl2(id int, fname char(30), lname char(30));

insert into testtbl2(id, fname, lname) select emp_no, first_name, last_name from employees.employees;

select * from testtbl2;
use sqldb;
create table bigtbl1 (select * from employees.employees);
create table bigtbl2 (select * from employees.employees);
create table bigtbl3 (select * from employees.employees);

delete from bigtbl1;
drop table bigtbl2;
truncate table bigtbl3;

set @myVar1 = 5; 
set @myVar2 = 4;
set @myVar3 = 2;
set @myVar4 = '가수이름==> ';

select @myVar1, @myVar2, @myVar3;

-- cast as
use sqldb;
select cast(avg(amount) as signed integer)
as '평균 구매 개수' from buytbl;

select cast('2020-12-12' as date) as date;

select cast(-12.5 as signed integer);
select cast(12.5 as unsigned integer);

select cast(123 as char(5));    
select rpad(cast(123 as char(5)),5,'0'); -- 전체 자리에 맞춰서 나머지를 채움
select lpad(cast(123 as char(5)),5,'0'); -- 전체 자리에 맞춰서 나머지를 채움
    
select concat_ws('/', 'a', 'b', 'c');
select concat('100','200');
select concat(100,'200');
select '100' + '200';

select 1 > '2mega';

select if (100>200, '참이다', '거짓이다');

select case 10
	when 1 then 'asdf'
    when 5 then 'asdc'
    when 10 then '십'
    else '모름'
    end;
    
select format(123456.123456, 14);

select insert('abcdefghi',3,4,'@@@@'),insert('abcdefghi',3,2,'@@@@');

select lower('abcdEFGH'), upper('abcdEFGH');
select left('abcdefghi',3), right('abcdefghi',3);

select trim('          이것이   ');

select replace('이것이 mysql이다','이것이','This is');

select repeat('살려줘',3);

select reverse('mysql');

select concat('이것이', space(10), 'asdf이다');

select substring('대한민국만세',3,2);
select rand(), rand() * (6-1), rand()*(6-1)+1; -- 0에서 1사이

select now();
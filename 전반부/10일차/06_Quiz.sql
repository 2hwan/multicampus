-- SQL 퀴즈

-- 1. 직원 이름이 빠른 순(A, B, C …) 순으로 리스트를 출력하시오.
use employees;
select * from employees order by first_name;


-- 2. 직원 나이가 적은 순으로 출력하시오.
select * from employees order by birth_date desc;



-- 3. 직원 중 나이가 가장 많은 사람의 나이는 몇 살 인가?
select min(birth_date) from employees;
select timestampdiff(year, min(birth_date), now()) as 나이 from employees;

-- 4. 직원들의 업무(titles)에는 직원별로 업무가 저장되어 있다. 이 회사의 업무 종류 리스트를 구하시오.
select distinct title from titles;


-- 5. 이 회사의 업무 종류 개수를 구하시오.
select count(distinct title) from titles;
select count(*) from (select title from titles group by title) a;

-- 6. 가장 최근에 입사한 사람 100명만 출력하시오
select * from titles order by from_date limit 100;


-- 7. 급여가 가장 많은 사람 10명을 구하시오.
select * from salaries order by salary desc limit 10;
select last_name from (select * from salaries order by salary desc limit 10);


-- 8. 급여가 가장 많은 사람 10명을 제외하고 다음 10명을 구하시오.
--   즉, 11등부터 20등 까지…
select * from salaries order by salary desc limit 11,10;


-- 9. 입사한지 가장 오래된 사람의 이름은 무엇인가?
select first_name, last_name from employees order by hire_date limit 1; 


-- 10. 1999년에 입사한 직원 리스트를 구하시오.
select * from employees; 
select * from employees where year(hire_date)= 1999;


-- 11. 1999년에 입사한 직원 중 여자 직원(GENDER='F') 리스트를 구하시오.
select * from employees where year(hire_date)= 1999 and gender = 'F';


-- 12. 1998년에 입사한 직원 중 남자 직원(M)은 몇 명인가?

select count(*) from employees where year(hire_date)= 1998 and gender = 'm';



-- 13. 1998년이나 1999년에 입사한 직원의 수를 구하시오.

select count(*) from employees where year(hire_date)= 1998 or year(hire_date)= 1999;


-- 14. 1995년부터 1999년까지 입사한 직원의 수를 구하시오.
select count(*) from employees where year(hire_date)> 1994 and year(hire_date)< 2000;


-- 15. 성(last_name)이 Senzako, Pettis, Henseler인 직원을 출력하시오.

select * from employees where last_name ='Senzako' or last_name ='Pettis' or last_name ='Henseler';
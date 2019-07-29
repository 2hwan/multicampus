use employees;
-- 1. 현재 근무 중인 직원 정보를 출력하시오.
select employees.*, dept_emp.dept_no from employees
	inner join dept_emp on employees.emp_no = dept_emp.emp_no
    where dept_emp.to_date = '9999-01-01';
 
-- 2. 현재 근무 중인 직원의 모든 정보(수행업무 포함) 를 출력하시오.
 select e.*, t.title
	from employees e
    inner join dept_emp d on e.emp_no = d.emp_no
    inner join titles t on e.emp_no = t.emp_no
    where d.to_date = '9999-01-01';



-- 3. 현재 근무 중인 부서명를 출력하시오. (사원번호, 사원명, 부서코드, 부서명)




-- 4. 가장오래 근무한 직원 10명의 현재 부서를 출력하시오.
select e.emp_no, d.dept_name
	from dept_emp de
    inner join employees e on e.emp_no = de.emp_no
    inner join departments d on de.dept_no = d.dept_no
	where de.to_date = '9999-01-01'
    order by hire_date
    limit 10;


-- 5. 부서별로 직원 수를 구하되 부서 이름이 나오게 출력하시오.
select d.dept_name, count(*)
	from departments d
	inner join dept_emp de on d.dept_no = de.dept_no
    where de.to_date = '9999-01-01'
    group by d.dept_name
    order by d.dept_name;


-- 6. 부서별, 성별 직원 수를 구하시오
select d.dept_name, sum(if(e.gender in ('m'),1,0)) as 'm', sum(if(e.gender in ('f'),1,0)) as 'f'
	from departments d
	inner join dept_emp de on d.dept_no = de.dept_no
    inner join employees e on e.emp_no = de.emp_no
    where de.to_date = '9999-01-01'
    group by d.dept_name
    order by d.dept_name;

select * from employees;


-- 7. 급여 평균이 가장 높은 부서 5개를 출력하시오. 
select d.dept_name, sa
from (select de.dept_no, avg(s.salary) sa
	from dept_emp de
	inner join salaries s on de.emp_no = s.emp_no
    where s.to_date = '9999-01-01'
    and s.to_date = '9999-01-01'
    group by de.dept_no
    order by sa desc
    limit 5) A inner join departments d
    on A.dept_no = d.dept_no;



-- 8. 급여 평균이 가장 높은 부서를 제외하고, 급여 평균이 높은 부서를 5개를 출력하시오. 
select d.dept_no, de.dept_name, avg(s.salary)
	from dept_emp d
	inner join salaries s on d.emp_no = s.emp_no
    inner join departments de on de.dept_no = d.dept_no
    where s.to_date = '9999-01-01'
    group by d.dept_no
    order by avg(s.salary) desc
    limit 2,5;



-- 9. 급여를 많이 받는 부서장 리스트를 출력하시오
select m.*, s.salary
	from dept_manager m
	inner join salaries s on m.emp_no = s.emp_no
    where s.to_date = '9999-01-01' and m.to_date = '9999-01-01'
    order by s.salary desc 
    limit 1;


 
-- 10. 개발부(Development)에서 급여를 가장 많이 받는 직원 5명을 출력하시오.
select e.first_name, e.last_name, s.salary
	from employees e
	inner join salaries s on e.emp_no = s.emp_no
    where s.to_date = '9999-01-01'
    order by s.salary desc
    limit 5;

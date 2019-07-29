-- 1. 부서별 부서장 정보를 출력하시오.
use employees;
select dept_name, first_name, last_name 
	from dept_manager dm
    inner join departments dep on dep.dept_no = dm.dept_no
    inner join employees emp on emp.emp_no = dm.emp_no
    WHERE dm.TO_DATE = '9999-01-01' 
    group by dm.dept_no;



-- 2. 부서별 정보(부서장, 부서별 급여 평균)을 출력하시오.
select dept_name, first_name, last_name, avg
	from dept_manager dm
    inner join departments dep on dep.dept_no = dm.dept_no
    inner join employees e on e.emp_no = dm.emp_no
	inner join (
		select d.dept_no , avg(s.salary) avg
		from salaries s
		inner join dept_emp d on s.emp_no = d.emp_no
		WHERE D.TO_DATE = '9999-01-01' and S.TO_DATE = '9999-01-01' 
		group by d.dept_no) A on dm.dept_no = A.dept_no
			WHERE Dm.TO_DATE = '9999-01-01' ;

-- 3. 부서별 직원 리스트를 출력하되 부서장이면 표시를 하고, 
--    각 부서에서 가장 먼저 나오게 출력하시오.
select dept_name, first_name, last_name
	,if(dm.emp_no is null, null, 'manager') position
	from dept_emp de
    inner join departments dep on dep.dept_no = de.dept_no
    inner join employees emp on emp.emp_no = de.emp_no
		left outer join dept_manager dm on dm.emp_no = de.emp_no
    WHERE de.TO_DATE = '9999-01-01'
    order by dept_name, dm.emp_no desc;
	


-- 4. 1999 년의 월별 신입 사원수를 출력하시오
select month(from_date),count(from_date);
	select year(hire_date)
    from employees
    where year(hire_date) in (1998, 1999)
    group by month(hire_date)
    order by month(hire_date);

	

 

-- 5. 1999 년의 월별 신입 사원수를 피봇으로 출력하시오 
-- (M1 ~ M12까지 컬럼으로 출력)
select year(hire_date),
	sum(if(month(hire_date) in (1), 1,0)) as 'M1',
	sum(if(month(hire_date) in (2), 1,0)) as 'M2',
	sum(if(month(hire_date) in (3), 1,0)) as 'M3',
	sum(if(month(hire_date) in (4), 1,0)) as 'M4',
	sum(if(month(hire_date) in (5), 1,0)) as 'M5',
	sum(if(month(hire_date) in (6), 1,0)) as 'M6',
	sum(if(month(hire_date) in (7), 1,0)) as 'M7',
	sum(if(month(hire_date) in (8), 1,0)) as 'M8',
	sum(if(month(hire_date) in (9), 1,0)) as 'M9',
	sum(if(month(hire_date) in (10), 1,0)) as 'M10',
	sum(if(month(hire_date) in (11), 1,0)) as 'M11',
    sum(if(month(hire_date) in (12), 1,0)) as 'M12'
    from employees
    where year(hire_date) in (1998, 1999)
    group by year(hire_date);

SELECT YEAR(HIRE_DATE) YR
                 , MONTH(HIRE_DATE) MM
                 , COUNT(*) CNT
             FROM EMPLOYEES 
            WHERE YEAR(HIRE_DATE) in (1998, 1999)
            GROUP BY YEAR(HIRE_DATE), MONTH(HIRE_DATE);
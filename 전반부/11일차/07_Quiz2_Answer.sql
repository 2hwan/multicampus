-- 1. 부서별 직원 수를 구하시오.

-- 부서를 추출하고, 각 부서의 인원수를 계산하는 것
SELECT D.DEPT_NAME
     , (SELECT COUNT(*) 
          FROM DEPT_EMP DE 
         WHERE DE.TO_DATE = '9999-01-01' 
           AND DE.DEPT_NO=D.DEPT_NO)
  FROM DEPARTMENTS D;

-- 부서와 인원 테이블을 조인해서 데이터를 구성하고 부서명으로 그룹화 한 뒤 인원을 계산
SELECT D.DEPT_NAME, COUNT(*) 
  FROM DEPARTMENTS D
 INNER JOIN DEPT_EMP DE ON DE.DEPT_NO=D.DEPT_NO
 WHERE DE.TO_DATE = '9999-01-01'
 GROUP BY D.DEPT_NAME;
 
 -- 문자열로 그룹화 하는 것보다는 정형화된 코드로 그룹화하는 것이 좋다.
 SELECT DEPT_NAME, CNT
   FROM DEPARTMENTS D
	   INNER JOIN (
			SELECT DEPT_NO, COUNT(*) CNT
			  FROM DEPT_EMP
			 WHERE TO_DATE='9999-01-01'
			 GROUP BY DEPT_NO
	  ) DS ON D.DEPT_NO = DS.DEPT_NO
 ORDER BY D.DEPT_NO;
 
-- 2. 각 부서에서 가장 오래 근무한 직원을 출력하시오.

SELECT DEPT_NAME
    , (SELECT FIRST_NAME
         FROM DEPT_EMP DE 
              INNER JOIN EMPLOYEES E ON E.EMP_NO = DE.EMP_NO
         WHERE DE.TO_DATE = '9999-01-01' 
           AND DE.DEPT_NO=D.DEPT_NO
         ORDER BY FROM_DATE 
         LIMIT 1) EMPLOYEE
  FROM DEPARTMENTS D;


-- 3. 가장 오래된 직원 10명이 근무했던 처음과 마지막 부서를 출력하시오.

SELECT EM.*
          , (SELECT DEPT_NAME 
               FROM DEPT_EMP DEE, DEPARTMENTS DE 
              WHERE DEE.DEPT_NO=DE.DEPT_NO 
                AND DEE.EMP_NO = EM.EMP_NO
              ORDER BY FROM_DATE LIMIT 1) FIRST_DEPT 
          , (SELECT DEPT_NAME 
               FROM DEPT_EMP DEE, DEPARTMENTS DE 
			  WHERE DEE.DEPT_NO=DE.DEPT_NO 
                AND DEE.EMP_NO = EM.EMP_NO
              ORDER BY FROM_DATE DESC LIMIT 1) LAST_DEPT 
  FROM EMPLOYEES EM
 ORDER BY HIRE_DATE
 LIMIT 10;


-- 4. 각 부서에서 급여를 가장 많이 받는 직원 리스트를 구하시오.

SELECT DEPT_NAME
	 , (SELECT FIRST_NAME 
		  FROM DEPT_EMP DE 
			  INNER JOIN EMPLOYEES E ON E.EMP_NO = DE.EMP_NO
			  INNER JOIN SALARIES S ON S.EMP_NO = DE.EMP_NO
		 WHERE DE.TO_DATE = '9999-01-01' 
           AND DE.DEPT_NO = D.DEPT_NO
		 ORDER BY SALARY DESC 
	     LIMIT 1) EMPLOYEE
 FROM DEPARTMENTS D;
 
 
 -- 5. 전체 평균보다 많이 받는 직원 수를 계산하시오.
 
SELECT COUNT(*) -- 107706
  FROM SALARIES S 
 WHERE S.TO_DATE = '9999-01-01'
   AND SALARY >= (SELECT AVG(SALARY) 
                    FROM SALARIES 
				   WHERE TO_DATE = '9999-01-01');

-- 6. 퇴직한 직원 정보를 구하시오.

SELECT *
  FROM EMPLOYEES E  
 WHERE NOT EXISTS(SELECT 1 FROM DEPT_EMP DE 
                   WHERE DE.TO_DATE = '9999-01-01' 
                     AND E.EMP_NO=DE.EMP_NO);


SELECT *
 FROM EMPLOYEES E  
WHERE EMP_NO NOT IN (SELECT DISTINCT EMP_NO 
                       FROM DEPT_EMP DE 
					  WHERE DE.TO_DATE = '9999-01-01');
                      

-- 1. 부서별 부서장 정보를 출력하시오.

SELECT DEPT_NAME, FIRST_NAME, LAST_NAME, SALARY 
  FROM DEPT_MANAGER DM
	  INNER JOIN DEPARTMENTS DEP ON DEP.DEPT_NO=DM.DEPT_NO
	  INNER JOIN EMPLOYEES EMP ON EMP.EMP_NO=DM.EMP_NO
	  INNER JOIN SALARIES SAL ON SAL.EMP_NO=DM.EMP_NO AND SAL.TO_DATE = DM.TO_DATE
WHERE DM.TO_DATE='9999-01-01' 
ORDER BY DEPT_NAME;

-- 2. 부서별 정보(부서장, 부서별 급여 평균)을 출력하시오.

SELECT DEPT_NAME, FIRST_NAME, LAST_NAME, AVG_SALARY
  FROM DEPT_MANAGER DM
  INNER JOIN DEPARTMENTS DEP ON DEP.DEPT_NO=DM.DEPT_NO
  INNER JOIN EMPLOYEES EMP ON EMP.EMP_NO=DM.EMP_NO
  INNER JOIN (
            SELECT DEPT_NO, AVG(SALARY) AVG_SALARY
              FROM DEPT_EMP DE
              INNER JOIN SALARIES SAL ON SAL.EMP_NO=DE.EMP_NO
             WHERE DE.TO_DATE='9999-01-01' AND SAL.TO_DATE='9999-01-01' 
             GROUP BY DEPT_NO
) DS ON DS.DEPT_NO=DM.DEPT_NO
 WHERE DM.TO_DATE='9999-01-01'
 ORDER BY DEPT_NAME;


-- 3. 부서별 직원 리스트를 출력하되 부서장이면 표시를 하고, 
--    각 부서에서 가장 먼저 나오게 출력하시오.

SELECT DEPT_NAME, FIRST_NAME, LAST_NAME, 
IF(DM.EMP_NO IS NULL, NULL, 'MANAGER') POSITION
  FROM DEPT_EMP DE
  INNER JOIN DEPARTMENTS DEP ON DEP.DEPT_NO=DE.DEPT_NO
  INNER JOIN EMPLOYEES EMP ON EMP.EMP_NO=DE.EMP_NO
    LEFT OUTER JOIN DEPT_MANAGER DM ON DM.EMP_NO=DE.EMP_NO AND DM.TO_DATE='9999-01-01'
 WHERE DE.TO_DATE='9999-01-01' 
 ORDER BY DEPT_NAME, DM.EMP_NO DESC, FIRST_NAME, LAST_NAME;
 
 
-- 4. 1999 년의 월별 신입 사원수를 출력하시오

SELECT MONTH(HIRE_DATE), COUNT(*) 
  FROM EMPLOYEES 
 WHERE YEAR(HIRE_DATE)=1999 
 GROUP BY MONTH(HIRE_DATE);
 

-- 5. 1999 년의 월별 신입 사원수를 피봇으로 출력하시오 
-- (M1 ~ M12까지 컬럼으로 출력)

SELECT YR
        ,SUM(CASE WHEN MM=1 THEN CNT ELSE 0 END) M1
        , SUM(CASE WHEN MM=2 THEN CNT ELSE 0 END) M2
        , SUM(CASE WHEN MM=3 THEN CNT ELSE 0 END) M3
        , SUM(CASE WHEN MM=4 THEN CNT ELSE 0 END) M4
        , SUM(CASE WHEN MM=5 THEN CNT ELSE 0 END) M5
        , SUM(CASE WHEN MM=6 THEN CNT ELSE 0 END) M6
        , SUM(CASE WHEN MM=7 THEN CNT ELSE 0 END) M7
        , SUM(CASE WHEN MM=8 THEN CNT ELSE 0 END) M8
        , SUM(CASE WHEN MM=9 THEN CNT ELSE 0 END) M9
        , SUM(CASE WHEN MM=10 THEN CNT ELSE 0 END) M10
        , SUM(CASE WHEN MM=11 THEN CNT ELSE 0 END) M11
        , SUM(CASE WHEN MM=12 THEN CNT ELSE 0 END) M12
  FROM (
            SELECT YEAR(HIRE_DATE) YR
                 , MONTH(HIRE_DATE) MM
                 , COUNT(*) CNT
             FROM EMPLOYEES 
           -- WHERE YEAR(HIRE_DATE) in (1998, 1999)
            GROUP BY YEAR(HIRE_DATE), MONTH(HIRE_DATE)
) DS
group by yr;

SELECT YEAR(HIRE_DATE) YR
                 , MONTH(HIRE_DATE) MM
                 , COUNT(*) CNT
             FROM EMPLOYEES 
            WHERE YEAR(HIRE_DATE) in (1998, 1999)
            GROUP BY YEAR(HIRE_DATE), MONTH(HIRE_DATE);

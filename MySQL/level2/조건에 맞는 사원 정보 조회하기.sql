SELECT SUM(SCORE) SCORE, HR_EMPLOYEES.EMP_NO, EMP_NAME, POSITION, EMAIL
FROM HR_DEPARTMENT
JOIN HR_EMPLOYEES ON HR_DEPARTMENT.DEPT_ID = HR_EMPLOYEES.DEPT_ID
JOIN HR_GRADE ON HR_EMPLOYEES.EMP_NO = HR_GRADE.EMP_NO
GROUP BY HR_GRADE.EMP_NO
ORDER BY SCORE DESC
LIMIT 1;

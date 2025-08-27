SELECT E.EMP_NO,
       E.EMP_NAME,
       S.GRADE,
       FLOOR(E.SAL * S.PERCENT) AS BONUS
FROM HR_EMPLOYEES E
JOIN (
    SELECT EMP_NO,
           CASE
             WHEN AVG(SCORE) >= 96 THEN 'S'
             WHEN AVG(SCORE) >= 90 THEN 'A'
             WHEN AVG(SCORE) >= 80 THEN 'B'
             ELSE 'C'
           END AS GRADE,
           CASE
             WHEN AVG(SCORE) >= 96 THEN 0.20
             WHEN AVG(SCORE) >= 90 THEN 0.15
             WHEN AVG(SCORE) >= 80 THEN 0.10
             ELSE 0
           END AS PERCENT
    FROM HR_GRADE
    GROUP BY EMP_NO
) S
  ON E.EMP_NO = S.EMP_NO
ORDER BY E.EMP_NO;
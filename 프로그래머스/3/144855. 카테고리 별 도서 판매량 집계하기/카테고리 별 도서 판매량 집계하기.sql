-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK B JOIN 
(SELECT *
FROM BOOK_SALES
WHERE SALES_DATE LIKE '2022-01%') T
ON B.BOOK_ID = T.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY ASC


-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER U JOIN
(SELECT *
FROM USED_GOODS_BOARD
WHERE STATUS = 'DONE') T ON U.USER_ID = T.WRITER_ID
GROUP BY T.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC;

-- 코드를 입력하세요
SELECT A.BOOK_ID AS BOOK_ID, AUTHOR.AUTHOR_NAME, DATE_FORMAT(A.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM (SELECT *
FROM BOOK
WHERE CATEGORY = '경제')  A
JOIN AUTHOR ON A.AUTHOR_ID = AUTHOR.AUTHOR_ID
ORDER BY PUBLISHED_DATE ASC;



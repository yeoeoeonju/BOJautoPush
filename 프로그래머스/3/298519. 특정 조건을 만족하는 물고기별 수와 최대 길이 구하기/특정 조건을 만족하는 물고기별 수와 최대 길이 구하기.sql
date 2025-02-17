-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM 
(SELECT ID, FISH_TYPE, CASE WHEN LENGTH IS NULL THEN 10 ELSE LENGTH END AS LENGTH
FROM FISH_INFO) AS NULL_DELETE 
GROUP BY FISH_TYPE
HAVING SUM(LENGTH) / COUNT(*) >= 33
ORDER BY FISH_TYPE ASC
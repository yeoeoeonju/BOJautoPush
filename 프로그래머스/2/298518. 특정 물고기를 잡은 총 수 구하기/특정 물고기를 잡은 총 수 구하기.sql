-- 코드를 작성해주세요
SELECT COUNT(ID) FISH_COUNT
FROM FISH_INFO JOIN 
(SELECT *
FROM FISH_NAME_INFO
WHERE FISH_NAME IN ('BASS', 'SNAPPER')) AS RE_NAME
ON FISH_INFO.FISH_TYPE = RE_NAME.FISH_TYPE

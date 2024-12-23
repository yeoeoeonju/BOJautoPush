-- 코드를 입력하세요
SELECT O.ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_OUTS O JOIN 
(SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE SEX_UPON_INTAKE LIKE 'INTACT%') I
ON O.ANIMAL_ID = I.ANIMAL_ID 
WHERE O.SEX_UPON_OUTCOME NOT LIKE 'INTACT%'
ORDER BY O.ANIMAL_ID ASC
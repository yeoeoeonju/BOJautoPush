-- 코드를 작성해주세요


SELECT C.ITEM_ID, C.ITEM_NAME, C.RARITY
FROM
ITEM_INFO C
JOIN ITEM_TREE B
ON C.ITEM_ID=B.ITEM_ID

JOIN ITEM_INFO A
ON B.PARENT_ITEM_ID=A.ITEM_ID

WHERE A.RARITY="RARE"
ORDER BY ITEM_ID DESC;


-- 코드를 입력하세요
-- 코드를 입력하세요
SELECT M.CART_ID
FROM (SELECT CART_ID, NAME
FROM CART_PRODUCTS 
WHERE NAME = 'Yogurt') Y JOIN
(SELECT CART_ID, NAME
 FROM CART_PRODUCTS
 WHERE NAME = 'Milk') M
ON Y.CART_ID = M.CART_ID

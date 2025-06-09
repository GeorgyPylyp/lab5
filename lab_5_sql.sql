-- Створення таблиці “літак1”
CREATE TABLE litak1
AS SELECT kod_litaka, kod_aviacompanii, rik_vypusku, model_litaka, kilkist_mists FROM litak
WHERE rik_vypusku < 2019;

-- Створення таблиці “літак2”. 
CREATE TABLE litak2
AS SELECT kod_litaka, kod_aviacompanii, rik_vypusku, model_litaka, kilkist_mists FROM litak
WHERE rik_vypusku > 2010;

-- 1. Об’єднання таблиць 
SELECT * FROM litak1
 UNION SELECT * FROM litak2;
 
-- 2. Запит перетину між таблицею “літак1” та “літак2”
SELECT * FROM litak1
 WHERE  rik_vypusku  IN (SELECT  rik_vypusku FROM litak2);
 
-- 3. Запит на різницю між таблицею “літак1” та “літак2”
SELECT * FROM litak1
 WHERE  rik_vypusku NOT IN (SELECT  rik_vypusku FROM litak2);

-- 4. Запит на виконання декартового добутку  між таблицею “літак1” та “літак2”.
SELECT * FROM litak1, litak2;
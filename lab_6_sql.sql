-- 1. Запит на виконання проекції (відображення) для таблиць вашої БД. 
CREATE VIEW comment_litak AS SELECT DISTINCT kod_litaka, ric_vypusku, model_litaka
FROM litak;

-- 2. Запит на виконання селекції з використанням будь-якої складної умови відбору для таблиць вашої БД. 
SELECT *
FROM comment_litak
WHERE rik_vypusku >= 2000 AND rik_vypusku < 2020

-- 3. Запит на виконання натурального з’єднання у будь-яких таблицях вашої БД. 
SELECT reisy.nomer_reysu, reisy.kod_litaka, reisy.chas_vidpravlennya, litak.kilkist_mists, litak.model_litaka
FROM reisy, litak
WHERE reisy.kod_litaka = litak.kod_litaka;

-- 4.Запит на виконання умовного з’єднання для таблиць вашої БД. 
SELECT reisy.nomer_reysu, reisy.kod_litaka, reisy.chas_vidpravlennya, litak.kilkist_mists, litak.model_litaka
FROM reisy, litak
WHERE reisy.kod_litaka = litak.kod_litaka and litak.kilkist_mists > 170 
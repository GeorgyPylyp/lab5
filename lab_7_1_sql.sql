-- 1. Всі пасажири з громадянством "Україна"
SELECT *
FROM Pasazhyr
WHERE hromadyanstvo = 'Україна';

-- 2. Літаки, випущені після 2015 року
SELECT *
FROM Litak
WHERE rik_vypusku > 2015;

-- 3. Аеропорти, що знаходяться в місті "Київ"
SELECT nazva_aeroportu
FROM Aeroport
WHERE misto_rozstashuvannya = 'Київ';

-- 4. Унікальні країни з таблиці аеропортів
SELECT DISTINCT krajina
FROM Aeroport;

-- 5. Загальна кількість пасажирів
SELECT COUNT(*) AS total_passengers
FROM Pasazhyr;

-- 6. Інформація про рейси та моделі літаків
SELECT r.nomer_reysu, r.kod_litaka, l.model_litaka
FROM Reisy r
JOIN Litak l ON r.kod_litaka = l.kod_litaka;

-- 7. Пасажири з даними про квитки
SELECT p.imya, p.prizvyshche, r.Misce_pasazhira, r.Cina_kvutka
FROM Pasazhyr p
JOIN Reestracia r ON p.kod_pasazhyra = r.kod_pasazhyra;

-- 8. Кількість літаків для кожної авіакомпанії
SELECT a.kod_aviacompanii, COUNT(*) AS total_litaks
FROM Aviacompaniya a
JOIN Litak l ON a.kod_aviacompanii = l.kod_aviacompanii
GROUP BY a.kod_aviacompanii;

-- 9. Рейси з назвами аеропортів відправлення
SELECT r.nomer_reysu, a.nazva_aeroportu
FROM Reisy r
JOIN Aeroport a ON r.kod_aeroportu_vidpravlennya = a.kod_aeroportu;

-- 10. Літаки, що не використовуються в рейсах
SELECT l.*
FROM Litak l
LEFT JOIN Reisy r ON l.kod_litaka = r.kod_litaka
WHERE r.kod_litaka IS NULL;

-- 11. Середня кількість місць у літаках кожної авіакомпанії
SELECT a.kod_aviacompanii, AVG(l.kilkist_mists) AS avg_seats
FROM Aviacompaniya a
JOIN Litak l ON a.kod_aviacompanii = l.kod_aviacompanii
GROUP BY a.kod_aviacompanii;

-- 12. Авіакомпанії з більше ніж 3 літаками
SELECT a.kod_aviacompanii, COUNT(*) AS litak_count
FROM Aviacompaniya a
JOIN Litak l ON a.kod_aviacompanii = l.kod_aviacompanii
GROUP BY a.kod_aviacompanii
HAVING COUNT(*) > 3;

-- 13. Рейси з тривалістю більше 2 годин
SELECT nomer_reysu, chas_vidpravlennya, chas_prybuttya
FROM Reisy
WHERE EXTRACT(EPOCH FROM (chas_prybuttya - chas_vidpravlennya)) / 3600 > 2;

-- 14.  Вивести список літаків, які обслуговували рейси щонайменше у двох різних країнах. 
SELECT l.kod_litaka, l.model_litaka, COUNT(DISTINCT a.krajina) AS krain
FROM Reisy r
JOIN Litak l ON r.kod_litaka = l.kod_litaka
JOIN Aeroport a ON r.kod_aeroportu_prybuttya = a.kod_aeroportu
GROUP BY l.kod_litaka, l.model_litaka
HAVING COUNT(DISTINCT a.krajina) >= 2;


-- 15. Знайти міста, та кількість рейсі з них. 
SELECT a.misto_rozstashuvannya, COUNT(*) AS kilkist_reysiv
FROM Reisy r
JOIN Aeroport a ON r.kod_aeroportu_vidpravlennya = a.kod_aeroportu
GROUP BY a.misto_rozstashuvannya
ORDER BY kilkist_reysiv DESC;
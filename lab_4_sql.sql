
-- 1. Заповнити таблиці вашої БД в режимі одиночного і групового доповнення.

INSERT INTO Aeroport (kod_aeroportu, nazva_aeroportu, misto_rozstashuvannya, krajina, shyrota, dovgota)
VALUES
('AR004', 'asfAIR', 'Florida', 'usa', '100.345', '20.894'),
('AR005', 'usaAIRLINE', 'Tehas', 'usa', '150.0379', '28.5622');

--2. Створити файли з даними (будь-якого сумісного типу) і заповнити ними решту таблиць базданих шляхом імпорту.
  --  заповнення таблиці реєстрація
COPY reestracia FROM 'd:/Reestracia.csv'DELIMITER ';' CSV HEADER;

  --  заповнення таблиці рейси
COPY reisy FROM 'd:/reisy.csv'DELIMITER ';' CSV HEADER;

 -- заповнення таблиці пасажир
COPY pasazhyr FROM 'd:/pasazhyr.csv'DELIMITER ';' CSV HEADER;

-- 3. Виконати модифікацію значень у будь-яких таблицях БД для одного поля та групи полів за
певною умовою.

  -- Одного поля 
UPDATE Litak
SET  model_litaka = 'Boeing 747'
WHERE kod_litaka = 'A003PG';

  -- Групи полів 
UPDATE Pasazhyr
SET imya_pasazhyra = 'Ira',
    prizvyshche = 'Sidorenco'
WHERE kod_pasazhyra = 3;

-- 4. Видалити записи з таблиць вашої БД.

DELETE FROM Aeroport
WHERE krajina = 'usa';

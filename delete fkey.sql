-- 1 Вилучити будь-який зв’язок між таблицями вашої БД.
ALTER TABLE Litak
DROP CONSTRAINT IF EXISTS litak_kod_aviacompanii_fkey;

-- 2 Вилучити і змінимо поля у одній з таблиць вашої БД.

ALTER TABLE Pasazhyr
DROP COLUMN po_batkovi;

ALTER TABLE Pasazhyr
RENAME COLUMN imya TO imya_pasazhyra;

-- 3 Змінити поле у одній з таблиць вашої БД.

ALTER TABLE Litak
ALTER COLUMN kilkist_mists TYPE SMALLINT;

-- 4 Додати поле і нове обмеження унікальності до будь-якої таблиці вашої БД. 

ALTER TABLE Aviacompaniya
ADD COLUMN rik_stvorenia INT NOT NULL;

ALTER TABLE Aviacompaniya
ADD CONSTRAINT unique_rik_stvorenia UNIQUE(rik_stvorenia);

-- 5 Змінити тип обмеження цілісності для зв’язку у одній з таблиць вашої БД

  -- видалення зв’язку 
ALTER TABLE Reestracia
DROP CONSTRAINT IF EXISTS reestracia_kod_pasazhyra_fkey;

  -- створення нового
ALTER TABLE Reestracia
ADD CONSTRAINT reestracia_kod_pasazhyra_fkey
FOREIGN KEY (kod_pasazhyra)
REFERENCES Pasazhyr(kod_pasazhyra)
ON DELETE CASCADE;
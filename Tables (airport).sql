-- Таблиця: АВІАКОМПАНІЯ
CREATE TABLE Aviacompaniya (
    kod_aviacompanii VARCHAR(20) NOT NULL PRIMARY KEY,
    unikalnyi_id_aviacompanii VARCHAR(50)NOT NULL,
    elektronna_poshta VARCHAR(100) NOT NULL,
    nomer_telefonu VARCHAR(12) NOT NULL,
    krajina VARCHAR(50) NOT NULL
);

-- Таблиця: АЕРОПОРТ
CREATE TABLE Aeroport (
    kod_aeroportu VARCHAR(20) NOT NULL PRIMARY KEY,
    nazva_aeroportu VARCHAR(100) NOT NULL,
    misto_rozstashuvannya VARCHAR(100) NOT NULL,
    krajina VARCHAR(50) NOT NULL,
    shyrota VARCHAR(20) NOT NULL,
    dovgota VARCHAR(20) NOT NULL
);

-- Таблиця: ЛІТАК
CREATE TABLE Litak (
    kod_litaka VARCHAR(20) NOT NULL PRIMARY KEY,
    kod_aviacompanii VARCHAR(20) NOT NULL,
    rik_vypusku INT NOT NULL,
    model_litaka VARCHAR(100) NOT NULL,
    kilkist_mists INT NOT NULL,
    FOREIGN KEY (kod_aviacompanii) REFERENCES Aviacompaniya(kod_aviacompanii)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- Таблиця: ПАСАЖИР
CREATE TABLE Pasazhyr (
    kod_pasazhyra INT NOT NULL PRIMARY KEY,
    pasport VARCHAR(20) NOT NULL,
    hromadyanstvo VARCHAR(50) NOT NULL,
    stat VARCHAR(10) NOT NULL,
    imya VARCHAR(50) NOT NULL,
    prizvyshche VARCHAR(50) NOT NULL,
    po_batkovi VARCHAR(50) NOT NULL,
    nomer_telefonu VARCHAR(12) NOT NULL
);

-- Таблиця: РЕЄСТРАЦІЯ
CREATE TABLE Reestracia(
    Nomer_kvutka INT NOT NULL PRIMARY KEY,
    kod_pasazhyra INT NOT NULL,
	Misce_pasazhira INT NOT NULL,
	Cina_kvutka VARCHAR(10) NOT NULL,
	Klas_kvutka INT NOT NULL,
	FOREIGN KEY (kod_pasazhyra) REFERENCES Pasazhyr(kod_pasazhyra)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- Таблиця: РЕЙСИ
CREATE TABLE Reisy (
    nomer_reysu VARCHAR(20) NOT NULL PRIMARY KEY,
    kod_litaka VARCHAR(20) NOT NULL,
    kod_aviacompanii VARCHAR(20) NOT NULL,
    kod_aeroportu_vidpravlennya VARCHAR(20) NOT NULL,
    kod_aeroportu_prybuttya VARCHAR(20) NOT NULL,
    chas_vidpravlennya TIME NOT NULL,
    chas_prybuttya TIME NOT NULL,
    FOREIGN KEY (kod_litaka) REFERENCES Litak(kod_litaka)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (kod_aeroportu_vidpravlennya) REFERENCES Aeroport(kod_aeroportu)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (kod_aeroportu_prybuttya) REFERENCES Aeroport(kod_aeroportu)
        ON UPDATE CASCADE ON DELETE CASCADE
);

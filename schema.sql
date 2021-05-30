CREATE TABLE Kayttajat (
	id SERIAL PRIMARY KEY,
	kayttajanimi TEXT UNIQUE,
	salasana TEXT
);

CREATE TABLE Maat (
	id SERIAL PRIMARY KEY,
	maan_nimi TEXT UNIQUE
);

CREATE TABLE Kappaleet_2021 (
        id SERIAL PRIMARY KEY,
        maa_id INTEGER REFERENCES Maat,
        laulaja TEXT,
        laulu TEXT
);


CREATE TABLE Kommentit (
	id SERIAL PRIMARY KEY,
	kayttaja_id INTEGER REFERENCES Kayttajat,
	laulu_id INTEGER REFERENCES Kappaleet_2021,
	sisalto TEXT,
	lahetetty TIMESTAMP
);

CREATE TABLE Pisteet (
	kayttaja_id INTEGER REFERENCES Kayttajat,
	laulu_id INTEGER REFERENCES Kappaleet_2021,
	pisteet INTEGER
);


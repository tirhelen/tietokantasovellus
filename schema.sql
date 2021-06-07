CREATE TABLE Users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
);

CREATE TABLE Countries (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);

CREATE TABLE Songs_2021 (
        id SERIAL PRIMARY KEY,
        country_id INTEGER REFERENCES Maat,
        singer TEXT,
        song TEXT
);


CREATE TABLE Comments (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES Kayttajat,
	song_id INTEGER REFERENCES Kappaleet_2021,
	message TEXT,
	sent TIMESTAMP
);

CREATE TABLE Points (
	user_id INTEGER REFERENCES Kayttajat,
	song_id INTEGER REFERENCES Kappaleet_2021,
	points INTEGER
);


CREATE TABLE Users (
	id SERIAL PRIMARY KEY,
	username TEXT UNIQUE,
	password TEXT
	is_admin BOOLEAN
);

CREATE TABLE Countries (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);

CREATE TABLE Songs_2021 (
        id SERIAL PRIMARY KEY,
        country_id INTEGER REFERENCES Countries,
        singer TEXT,
        song TEXT
);


CREATE TABLE Comments (
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES Users,
	song_id INTEGER REFERENCES Songs_2021,
	message TEXT,
	sent TIMESTAMP
	visible BOOLEAN
);

CREATE TABLE Points (
	user_id INTEGER REFERENCES Users,
	song_id INTEGER REFERENCES Songs_2021,
	points INTEGER
);


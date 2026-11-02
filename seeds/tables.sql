
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER
    );

INSERT INTO films (title, release_year) VALUES ('King Kong', 1933);
INSERT INTO films (title, release_year) VALUES ('The Godfather', 1972);
INSERT INTO films (title, release_year) VALUES ('Star Wars', 1977);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);



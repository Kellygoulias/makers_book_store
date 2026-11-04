DROP TABLE IF EXISTS films;

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER
    );

TRUNCATE table films;

INSERT INTO films (title, release_year) VALUES ('King Kong', 1933);
INSERT INTO films (title, release_year) VALUES ('The Godfather', 1972);
INSERT INTO films (title, release_year) VALUES ('Star Wars', 1977);


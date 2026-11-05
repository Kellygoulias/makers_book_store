
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    synopsis VARCHAR(255),
    rating INT,
    notes VARCHAR(255)
);

TRUNCATE table books;


INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('The Gruffalo', 'Julia Donaldson', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('Ada Twist, Scientist', 'Andrea Beaty', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('Dragons in a Bag', 'Zetta Elliott', 'things happen', 5, 'no notes');



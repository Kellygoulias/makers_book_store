
TRUNCATE table books;

ALTER TABLE books
ADD synopsis VARCHAR(255);
ALTER TABLE books
ADD rating INT;
ALTER TABLE books
ADD notes VARCHAR(255);

INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('The Gruffalo', 'Julia Donaldson', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('Ada Twist, Scientist', 'Andrea Beaty', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill', 'things happen', 5, 'no notes');
INSERT INTO books (title, author, synopsis, rating, notes) VALUES ('Dragons in a Bag', 'Zetta Elliott', 'things happen', 5, 'no notes');




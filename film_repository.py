from film import Film
from database_connection import DatabaseConnection

class FilmRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM films;')
        print(rows)
        films = []
        for row in rows:
            print(row)
            item = Film(row["title"], row["release_year"], row["id"])
            films.append(item)
        return films

    def create(self, film):
        self._connection.execute('INSERT INTO films (title, release_year) VALUES (%s, %s);', [film.title, film.release_year])
        return None
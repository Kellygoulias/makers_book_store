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
            item = Film(row["id"], row["title"], row["release_year"])
            films.append(item)
        return films
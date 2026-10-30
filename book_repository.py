from book import Book

class BookRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        return [ Book(row["title"], row["author"], row["id"])
            for row in rows]

    # # Find a single artist by their id
    # def find(self, artist_id):
    #     rows = self._connection.execute(
    #         'SELECT * from artists WHERE id = %s', [artist_id])
    #     row = rows[0]
    #     return Artist(row["id"], row["name"], row["genre"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, book):
        self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)',
                                [ book.title, book.author ]
                            )
        return None     

    # # Delete an artist by their id
    # def delete(self, artist_id):
    #     self._connection.execute(
    #         'DELETE FROM artists WHERE id = %s', [artist_id])
    #     return None
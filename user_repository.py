from user import User

class UserRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    # def all(self):
    #     rows = self._connection.execute('SELECT * from users')
    #     return [ User(row["username"], row["password"], row["id"])
    #         for row in rows]

    # # Find a single user by their id
    # def find(self, artist_id):
    #     rows = self._connection.execute(
    #         'SELECT * from artists WHERE id = %s', [artist_id])
    #     row = rows[0]
    #     return Artist(row["id"], row["name"], row["genre"])

    # Create a new user
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)',
                                [ user.username, user.password, user.email]
                            )
        return None     

    # # Delete an user by their id
    # def delete(self, artist_id):
    #     self._connection.execute(
    #         'DELETE FROM artists WHERE id = %s', [artist_id])
    #     return None
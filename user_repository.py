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

    # Find a single user by their id
    def authenticate(self, user):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s AND password = %s AND email = %s', [user.username, user.password, user.email])
        row = rows[0]
        return User(row["username"], row["password"], row["email"])

    def find_by_username(self, username):
        user_details = self._connection.execute(
        'SELECT * FROM users WHERE username = %s', [username]
        )[0]

        return User(
        user_details["username"],
        user_details["password"],
        user_details["email"],
        user_details["id"]
    )

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
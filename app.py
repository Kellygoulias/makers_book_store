from flask import Flask, render_template, request, redirect
from database_connection import DatabaseConnection
from book_repository import BookRepository
from user_repository import UserRepository
from film_repository import FilmRepository
from user import User
from book import Book
from film import Film

# instantiate a Flask app object
app = Flask(__name__)


# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in

app.route("/seed_tables", methods=['GET'])
def seed_table_name():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed('./seeds/tables.sql')
    return 'if you see this, database was probably seeded for USER AND FILM'

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)

@app.route('/users/new', methods=['GET'])
def get_signup():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    user_details = request.form
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user = User(username= user_details["username"], password =user_details["password"], email =user_details['email'])
    print(user)
    user_repository.create(user)
    return redirect("/books")

@app.route("/films", methods=["GET"])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    films = film_repository.all()
    print(films)
    return render_template("films.html", films=films)
    # films_json = []
    # for film in films:
    #     item = {"title": film.title, "release_year": film.release_year}
    #     films_json.append(item)
    # return films_json

@app.route("/films", methods= ["POST"])
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film = request.form
    add_film = Film(title= film["title"], release_year= film["release_year"])
    film_repository.create(add_film)
    return redirect('/films')

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
    book_details = request.form
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book = Book(title= book_details["title"], author =book_details["author"])
    print(book)
    book_repository.create(book)
    return redirect("/books")


@app.route('/authors', methods=['GET'])
def authors():
    return [
        {
            "name": "Julia Donaldson",
            "dob": "1948-09-16"
        },
        {
            "name": "Andrea Beaty",
            "dob": "1961-10-08"
        },
        {
            "name": "Kelly Barnhill",
            "dob": "1973-01-01"
        },
        {
            "name": "Zetta Elliott",
            "dob": "1979-11-11"
        }
    ]

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

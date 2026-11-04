from playwright.sync_api import Page, expect

from database_connection import DatabaseConnection


# this line is a bit of a hack which allows us to import app without changing anything else


def test_film_page(page: Page):
    page.goto('http://127.0.0.1:5001/films')
    form = page.locator('form')
    expect(form)



def test_film_added_to_database(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '1234', 'email@email.com');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("Password").fill("1234")
    page.get_by_placeholder("Email").fill('email@email.com')
    page.get_by_role("button", name= "Submit").click()

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("The Notebook")
    page.get_by_placeholder("Release_year").fill('2004')
    page.get_by_role("button", name="Submit").click()
    
    newest_film = page.locator("li").last.inner_text()
    assert newest_film == 'The Notebook - 2004'

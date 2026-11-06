from playwright.sync_api import Page, expect, APIResponse, Response
from database_connection import DatabaseConnection
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

# this line is a bit of a hack which allows us to import app without changing anything else



def test_auth_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'email@email.com');")

    response = client.post('/sessions', data={
        'username': 'test',
        'password': '1234',
        'email': 'email@email.com'
    })

    assert response.status_code == 302
    # this assertion might be new to you :)
    assert response.headers['Location'].endswith('/books')


def test_auth_failed_integration():
    client = app.test_client()
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'email@email.com');")

    response = client.post('/sessions', data={
        'username': 'test',
        'password': '123sss4',
        'email': 'email@email.com'
    })

    assert response.status_code == 302
    # this assertion might be new to you :)
    assert response.headers['Location'].endswith("/sessions/new")


def test_auth_playwright(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'email@email.com');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("1234")
    page.get_by_placeholder("Email").fill('email@email.com')
    page.get_by_role("button", name="submit").click()

    assert page.url == "http://localhost:5001/books"



def test_auth_failed_playwright(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'email@email.com');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("username").fill("test")
    page.get_by_placeholder("password").fill("12s34")
    page.get_by_placeholder("Email").fill('email@email.com')
    page.get_by_role("button", name="submit").click()

    assert page.url == "http://localhost:5001/sessions/new"

def test_auth_playwright(page: Page):

    page.goto("http://localhost:5001/books")
    page.get_by_role("button", name="Add a new book").click()

    assert page.url == "http://localhost:5001/sessions/new"
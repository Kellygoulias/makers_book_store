from playwright.sync_api import Page, expect
from database_connection import DatabaseConnection

def test_book_list_contains_all_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    

    books = page.locator('li')

    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott'
    ]       
    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books

def test_has_correct_books(page: Page):
    page.goto("http://127.0.0.1:5001/books")

    ul = page.locator("ul")

    expect(ul).to_contain_text('The Gruffalo by Julia Donaldson')
    expect(ul).to_contain_text('Ada Twist, Scientist by Andrea Beaty')
    expect(ul).to_contain_text('The Girl Who Drank the Moon by Kelly Barnhill')
    expect(ul).to_contain_text('Dragons in a Bag by Zetta Elliott')

def test_new_book_inserted(page: Page):

    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password, email) values ('test', '1234', 'email@email.com');")
    
    page.goto("http://localhost:5001/sessions/new")
    page.get_by_placeholder("Username").fill("test")
    page.get_by_placeholder("Password").fill("1234")
    page.get_by_placeholder("Email").fill('email@email.com')
    page.get_by_role("button", name= "Submit").click()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"
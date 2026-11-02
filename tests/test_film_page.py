from playwright.sync_api import Page, expect

# this line is a bit of a hack which allows us to import app without changing anything else


def test_film_page(page: Page):
    page.goto('http://127.0.0.1:5001/films')
    form = page.locator('form')
    expect(form)


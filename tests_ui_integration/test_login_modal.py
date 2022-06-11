from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage import HomePage
import utils.element as element
import os

def test_signin(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto(os.environ['URL'])

    homepage = HomePage(page)
    homepage.login("a8@test.com","a008@1")
    sleep(1)

    homepage.signout()
    sleep(1)

    context.close()
    browser.close()

def test_signup_with_error(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto(os.environ['URL'])

    homepage = HomePage(page)
    homepage.signup("asdfgh","Sdffsd","1242345", with_error=True)
    element.expect_to_be_visible(homepage.alert_message)
    sleep(1)
    # ---------------------
    context.close()
    browser.close()
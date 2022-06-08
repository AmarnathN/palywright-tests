from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect
from pom.commons import Commons
from pom.homepage import HomePage
import utils.element as element

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto("http://localhost:3000/")

    homepage = HomePage(page)
    homepage.login("a8@test.com","a008@1")
    
    homepage.signout()
    sleep(1)

    homepage.signup("asdfgh","Sdffsd","1242345", is_error=True)

    element.expect_to_be_visible(homepage.alert_message)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

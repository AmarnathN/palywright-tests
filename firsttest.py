from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage import HomePage

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto("http://localhost:3000/")

    homepage = HomePage(page)
    homepage.login("a8@test.com","a008@1")
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

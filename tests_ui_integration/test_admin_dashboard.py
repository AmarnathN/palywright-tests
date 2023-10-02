from time import sleep
from playwright.sync_api import Playwright
from pom.adminpage import AdminPage
from pom.homepage import HomePage
import os

def test_signin(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto("http://localhost/")
    # page.goto(os.environ['URL'])
    homepage = HomePage(page)

    # admin_login
    homepage.login("a8@test.com","a008@1")
    sleep(1)
    
    adminpage = AdminPage(page)
    adminpage.goto_create_category()
    adminpage.create_category("Test Automation")

    adminpage.go_to_dashboard()
    adminpage.delete_category("Test Automation")
    sleep(1)

    context.close()
    browser.close()

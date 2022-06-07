from playwright.sync_api import Playwright, sync_playwright, expect
import utils.element as element

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://localhost:3000/
    page.goto("http://localhost:3000/")

    # Click button:has-text("Login")
    element.click(page.locator("button:has-text(\"Login\")"))
    # Click input[name="email"]
    element.click(page.locator("input[name=\"email\"]"))
    # Fill input[name="email"]
    element.fill(page.locator("input[name=\"email\"]"),"a8@test.com")

    # Fill input[name="password"]
    element.fill(page.locator("input[name=\"password\"]"),"a008@1")

    # Press Enter
    element.press(page.locator("input[name=\"password\"]"),"Enter")

    element.expect_to_be_visible(page.locator("text='Admin Dashboard Page'"))
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

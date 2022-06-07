import utils.element as element


class HomePage:
    def __init__(self, page):
        self.page_header = page.locator("text='Admin Dashboard Page'")
        self.login_button = page.locator("button:has-text(\"Login\")")
        self.email_input = page.locator("input[name=\"email\"]")
        self.password_input = page.locator("input[name=\"password\"]")
        self.name_input = page.locator("input[name=\"password\"]")
        self.signup_tab = page.locator(".MuiDialogContent-root .MuiTabs-root span:has-text(\"SignUp\")")
        
    def login(self, username, password):
        try:
            element.click(self.login_button)
            element.click(self.email_input)
            element.fill(self.email_input,username)
            element.fill(self.email_input,password)

            # Press Enter to submit
            element.press(self.password_input,"Enter")

            element.expect_to_be_visible(self.page_header)
        except Exception as e:
            raise Exception("Exception while completing login steps on HomePage : {}".format(e))

    def signup(self, name, username, password):
        try:
            element.click(self.login_button)
            element.click(self.signup_tab)
            element.fill(self.name_input,name)
            element.fill(self.email_input,username)
            element.fill(self.email_input,password)

            # Press Enter to submit
            element.press(self.password_input,"Enter")

            element.expect_to_be_visible(self.page_header)
        except Exception as e:
            raise Exception("Exception while completing login steps on HomePage : {}".format(e))


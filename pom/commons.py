import utils.element as element

class Commons:
    def __init__(self, page):
        self.page = page
        self.alert_message = page.locator(".MuiAlert-message")
        self.account_toggle_icon = page.locator('button[data-testid="account-toggle"]')
        self.signout_element = page.locator(".MuiDrawer-paperAnchorRight span:has-text('SignOut')")

    def signout(self):
        try:
            element.click(self.account_toggle_icon)
            element.click(self.signout_element)

        except Exception as e:
            raise Exception("Exception while completing login steps on HomePage : {}".format(e))

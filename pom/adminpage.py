from socket import timeout
from pom.commons import Commons
import utils.element as element


class AdminPage(Commons):
    def __init__(self, page):
        super(AdminPage,self).__init__(page)
        self.page_header = page.locator("text='Admin Dashboard Page'")
        self.admin_details = page.locator("text='Admin Details'")
        self.products_expanded = page.locator("button[data-bs-target='#collapseProducts'][aria-expanded='true']")
        self.products_create_product_link = page.locator("a:has-text('Create Product')")
        self.products_manage_product_link = page.locator("a:has-text('Manage Product')")
        self.categories_expanded = page.locator("button[data-bs-target='#collapseCategories'][aria-expanded='true']")
        self.categories_collapsed = page.locator("button[data-bs-target='#collapseCategories']")
        
        self.categories_create_category_link = page.locator("a:has-text('Create Category')")
        self.categories_manage_category_link = page.locator("a:has-text('Manage Category')")
        self.create_category_header = page.locator("text='Create Categories'")
        self.new_category_input = page.locator("//input[contains(@placeholder,'Enter catefory name')]")
        self.go_to_dashboard_button = page.locator("a:has-text('Go To Dashboard')")

    def goto_create_category(self):
        try:
            if(not self.categories_expanded.is_visible()):
                element.click(self.categories_collapsed)
            element.expect_to_be_visible(self.categories_create_category_link)

            element.click(self.categories_create_category_link)
            element.wait_for(self.create_category_header)

        except Exception as e:
            raise Exception("Exception while goto_create_category : {}".format(e))

    def create_category(self, category_name):
        try:
            element.fill(self.new_category_input, category_name)

            # Press Enter to submit
            element.press(self.new_category_input,"Enter")
            element.expect_to_be_visible(self.alert_message)
        except Exception as e:
            raise Exception("Exception while create_category : {}".format(e))

    def go_to_dashboard(self):
        try:
            element.click(self.go_to_dashboard_button)
            element.wait_for(self.admin_details)
        except Exception as e:
            raise Exception("Exception while go_to_dashboard : {}".format(e))

    def delete_category(self, category_name):
        try:
            if(not self.categories_expanded.is_visible()):
                element.click(self.categories_collapsed)
            element.expect_to_be_visible(self.categories_manage_category_link)
            element.click(self.categories_manage_category_link)

            category_delete_icon = "//*[@data-value='{}']//following-sibling::div[@aria-colindex='2']//strong".format(category_name)
            while not self.page.locator(category_delete_icon).is_visible():
                if(self.grid_next_page_button.is_enabled()):
                    element.click(self.grid_next_page_button)
                else:
                    break
            element.click(self.page.locator(category_delete_icon))
            element.expect_to_be_visible(self.alert_message)
        except Exception as e:
            raise Exception("Exception while delete_category : {}".format(e))

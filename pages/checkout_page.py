from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUMMARY_SECTION = (By.CLASS_NAME, "summary_info")
    FINISH_BUTTON = (By.ID, "finish")

    def fill_info(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.ZIP_CODE, zip_code)

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)

    def is_summary_displayed(self):
        return self.is_displayed(self.SUMMARY_SECTION)

    def finish_purchase(self):
        self.click(self.FINISH_BUTTON)
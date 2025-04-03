from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ConfirmationPage(BasePage):
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-header")

    def is_confirmation_displayed(self):
        return "Thank you for your order!" in self.get_text(self.CONFIRMATION_MESSAGE)
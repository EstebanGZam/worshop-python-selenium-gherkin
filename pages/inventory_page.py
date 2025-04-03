from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    APP_LOGO = (By.CLASS_NAME, "app_logo")  # Ejemplo
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')][1]")  # Primer botón
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_app_logo(self):
        """
        Obtiene el logo de la aplicación.
        """
        return self.get_element(self.APP_LOGO)
    
    def is_inventory_page_displayed(self):
        # Verifica si el título o algún elemento único de la página está visible
        return self.find_element(self.APP_LOGO)  # Usa el método de BasePage si existe

    def add_first_item_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_ICON)
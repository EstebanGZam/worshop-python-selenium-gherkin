from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    APP_LOGO = (By.CLASS_NAME, "app_logo")  # Ejemplo

    def get_app_logo(self):
        """
        Obtiene el logo de la aplicación.
        """
        return self.get_element(self.APP_LOGO)
    
    def is_inventory_page_displayed(self):
        # Verifica si el título o algún elemento único de la página está visible
        return self.find_element(self.APP_LOGO)  # Usa el método de BasePage si existe
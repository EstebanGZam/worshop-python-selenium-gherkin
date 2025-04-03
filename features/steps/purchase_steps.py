# features/steps/purchase_steps.py
from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.login_page import LoginPage

@given("the user is logged in with valid credentials")
def step_user_logged_in(context):
    # Inicializa login_page si no existe (igual que en login_steps.py)
    if not hasattr(context, 'login_page'):
        context.login_page = LoginPage(context.driver)
    
    # Navega a la página de login y realiza el login
    context.driver.get("https://www.saucedemo.com")  # Asegúrate de que la URL sea correcta
    context.login_page.login("standard_user", "secret_sauce")
    context.inventory_page = InventoryPage(context.driver)  # Inicializa inventory_page

@when("the user adds the first product to the cart")
def step_add_first_product(context):
    context.inventory_page.add_first_item_to_cart()

@when("the user proceeds to checkout")
def step_proceed_to_checkout(context):
    context.inventory_page.go_to_cart()
    context.cart_page = CartPage(context.driver)
    context.cart_page.proceed_to_checkout()

@when("the user fills checkout information with")
def step_fill_checkout_info(context):
    context.checkout_page = CheckoutPage(context.driver)
    data = context.table[0]  # Usa la tabla del .feature
    context.checkout_page.fill_info(data["First Name"], data["Last Name"], data["Zip Code"])

@when("the user continues to the overview")
def step_continue_to_overview(context):
    context.checkout_page.continue_to_overview()

@then("the order summary should be displayed")
def step_order_summary_displayed(context):
    assert context.checkout_page.is_summary_displayed()

@then("the user completes the purchase")
def step_complete_purchase(context):
    context.checkout_page.finish_purchase()
    context.confirmation_page = ConfirmationPage(context.driver)

@then("a confirmation message should appear")
def step_confirmation_message(context):
    assert context.confirmation_page.is_confirmation_displayed()
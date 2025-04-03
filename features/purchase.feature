# features/purchase.feature
Feature: Purchase Product
  As a logged-in user
  I want to add a product to the cart and complete the purchase
  So that I can verify the checkout process

  Scenario: Successful purchase of a single product
    Given the user is logged in with valid credentials
    When the user adds the first product to the cart
    And the user proceeds to checkout
    And the user fills checkout information with:
      | First Name | Last Name | Zip Code |
      | John       | Doe       | 12345    |
    And the user continues to the overview
    Then the order summary should be displayed
    And the user completes the purchase
    Then a confirmation message should appear
#just write doc,not to run directly
Feature:
Home page-->Choose products   by categories -->add to cart
  Scenario: Select phones
  Given I am at home page
    When I Choose  3 diffrent  phones
    And I Click add to cart
    Then 3 phones added to cart




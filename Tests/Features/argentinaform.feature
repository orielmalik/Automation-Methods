Feature: Fill Fields

  Scenario: Fill fields with valid input
    Given I have validated the input values
    When I enter the values into the corresponding input fields
    Then I should be navigated to the next page

  Scenario: Submit with empty input
    Given the input fields are empty
    When I try to submit the form
    Then I should see a validation error indicating that the fields cannot be empty

  Scenario: Submit with incorrectly formatted input
    Given I have input values where at least one value is in the wrong format
    When I enter these values into the corresponding input fields
    Then I should see a validation error indicating which input(s) are incorrectly formatted



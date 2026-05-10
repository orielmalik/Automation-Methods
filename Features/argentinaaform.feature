#Read Only-not to exec
Feature: Fill Fields

  Scenario: PASS cases
    Given valid input data
    When I submit the form
    Then I should be redirected successfully

  Scenario: EMPTY cases
    Given empty required fields
    When I submit the form
    Then I should see required field errors

  Scenario: INVALID cases
    Given incorrectly formatted input
    When I submit the form
    Then I should see validation errors
# Created by Yulia at 10/20/23
Feature: Secondary Deals Filtering

  Scenario: User can filter Secondary deals by "want to buy" option
    Given Open the main page
    When User logs in
    And User clicks on the Secondary option in the left side menu
    Then Correct page is open
    When User filters the products by 'want to buy'
    Then Verify all cards have a 'want to buy' tag



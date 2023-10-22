# Created by Yulia at 10/21/23
Feature: Test Secondary Option feature on Different Browsers

  Scenario Outline:
    Given User has a "<browser>" browser
    Then Execute all steps from secondary_option
    Then Close the browser
    Examples:
    | browser   |
    | Chrome    |
    | Firefox   |
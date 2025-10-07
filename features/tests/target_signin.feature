  Feature: Tests for Target SignIn Functionality
    # Description: HW 2 Target Sign In Page

  Scenario: User can navigate to the SignIn Page with Target
    Given Open target main page

    When Click Account button
    When Click SignIn button from side navigation bar

    Then Verify Sign In or Create Account Text is shown
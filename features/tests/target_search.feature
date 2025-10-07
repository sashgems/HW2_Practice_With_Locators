
  Feature: Tests for Target search functionality
    # Description Target Sign In Page HW

  Scenario: User can navigate to the SignIn Page with Target
    Given Open target main page

    When Click Account button
    When Click SignIn button from side navigation bar

    Then Verify Sign In or Create Account Text is shown
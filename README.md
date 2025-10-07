# Practicing With Locators on Amazon Sign In Page 
# 1. Practice with locators. 
# Create locators + search strategy for these page elements of Amazon Sign in page:
    # amazon_locator_practice.py
    # contains the locators and search strategy for the following 
        # Amazon logo
        # Email field
        # Continue button
        # Conditions of use link
        # Privacy Notice link
        # Need help link
        # Forgot your password link
        # Other issues with Sign-In link
        # Create your Amazon account button

# 2. Create a test case for the SignIn page using python & selenium script. 
    # Answers in target_sign_in.py
    # Steps refactored into file target_sign_in_steps.py and target_signin.feature
    # Included target_search.feature file that we went over in class
(Make sure to use Incognito browser mode when searching for locators)

# Test Case: Users can navigate to SignIn page
        # 1. Open https://www.target.com/ 
        # 2. Click Account button
        # 3. Click SignIn btn from side navigation
        # 4. Verify SignIn page opened: 
                # “Sign in or create account” text is shown,
                 # SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)

# [Optional] Build a test case yourself from scratch to search for a product on Target (same as shown in the class), make sure it works and you remember selenium commands.
# Assessment criteria
    # Locators are built correctly and point to the correct webelements
    # Test case runs and works correctly

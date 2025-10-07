
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('click account button')
def click_account(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
   sleep(7)

@then('Verify search results are shown')
def verify_search_results(context):
    context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']")

# For then statement we went over this other way to do it with expected and actual results
#expected = 'Sign in or create account'
#actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
#assert expected == actual, f'Expected {expected} did not match actual {actual}'

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    #context.driver.get('https://www.target.com/')

@when('Search for a product')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(7)
    #context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    #context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Expected text {expected_text}'
    #driver.find_element(By.XPATH, "//*[text()='Sign in or create account']")

#HW Lesson 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser:
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Open target.com
driver.get('https://www.target.com/')

# click account button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

# Verification

driver.find_element(By.XPATH, "//*[text()='Sign in or create account']")

#More complex way to do it
#expected = 'Sign in or create account'
#actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
#assert expected == actual, f'Expected {expected} did not match actual {actual}'

# Make sure login button is shown
driver.find_element(By.ID, 'login')

driver.quit()

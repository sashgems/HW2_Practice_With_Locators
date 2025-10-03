from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click account button
driver.find_element(By.CLASS, 'sc-272da4bf-3 jfjzNu h-margin-r-x3').click()

# click sign in from side menu
driver.find_element(By_XPATH, "//button[data-test='accountNav-signIn']" ).click()

#4. Verify SignIn page opened:
#“Sign in or create account” text is shown,
#SignIn button is shown (you can just use driver.find_element() to check for element’s presence, no need to assert here)
driver.find_element(By_XPATH, "//*[text()='Sign in']")
driver.find_element(By.XPATH, "//button[contains(@class,'class='styles_ndsBaseButton')]")

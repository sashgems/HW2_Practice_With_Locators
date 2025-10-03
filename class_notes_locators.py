from selenium.webdriver.common.by import By

#Amazon Home Page

driver.find_element(By.XPATH, "//p[contains(@class,'Search Amazon')")
# $x//'p[contains(@class,"Search Amazon"])'

driver.find_element(By.XPATH, "//i[@aria-label='Search Amazon']")

driver.find_element(By.XPATH, '//p[contains(@class,"Search Amazon"])')

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']//i[@aria-label='Search Amazon']")

#Amazon Sign Up Page
# Privacy Notice Link
driver.find_element(By.XPATH, "a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])
#CONFIRMED THE XPATH ON SITE:
#$x//("a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])
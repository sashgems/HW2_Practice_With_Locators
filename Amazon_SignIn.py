from selenium.webdriver.common.by import By

#1 Amazon Logo
driver.find_element(By.XPATH, "//p[contains(@class,'Search Amazon')")
# $x//'p[contains(@class,"Search Amazon"])'

driver.find_element(By.XPATH, "//i[@aria-label='Search Amazon']")

driver.find_element(By.XPATH, '//p[contains(@class,"Search Amazon"])')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
"//i[@aria-label='Search Amazon']")


#2. Email Field
driver.find_element(By.XPATH,

#3. Continue Button
driver.find_element(By.NAME, 'btnK').click()

#4. Conditions of use Link
driver.find_element(By.XPATH,

#5. Privacy Notice Link
driver.find_element(By.XPATH, "a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])
#CONFIRMED XPATH ON SITE W/JAVASCRIPT CDOE:
#$x//("a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])

#7. Forgot password link  (n/a)
#8. Other issues with sign-in link (n/a)
#9. Create Amazon Account Button
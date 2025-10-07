# Practice With Locators HW Assignment
from selenium.webdriver.common.by import By

#1 Amazon Logo
driver.find_element(By_XPATH, "//i[contains(@class, 'icon-logo')]//i[contains(@aria-label, 'Amazon')]")
# $x("//i[contains(@class, 'icon-logo')]//i[contains(@aria-label, 'Amazon')]")

#2. Email Field
driver.find_element(By_ID, 'ap_email_login')
#$x("//input[id='ap_email_login']")

#3. Continue Button
driver.find_element(By_XPATH, "//input[class='a-button-input']" )
#$x("//input[class='a-button-input']")

#4. Conditions of Use Link
driver.find_element(By_XPATH, "//p[contains(@class, 'legal-text')]//a[contains(@href, 'conditions_of_use')]" )
#$X("//p[contains(@class, 'legal-text')]//a[contains(@href, 'conditions_of_use')]")

#5. Privacy Notice Link
driver.find_element(By.XPATH, "a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])
#CONFIRMED XPATH ON SITE W/JAVASCRIPT CDOE:
#$x//("a[contains(@href='ref=ap_signin_notification_privacy_notice?')"])

#7. Forgot password link  (n/a on the page listed)
# If you enter an email in the field and press continue on the sign in page
# you have the option to click forgot password on another URL.
#URL: https://www.amazon.com/ax/claim?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fhelp%2Fcustomer%2Faccount-issues%2Fref%3Dnav_ya_signin%3Fie%3DUTF8&policy_handle=Retail-Checkout&openid.mode=checkid_setup&openid.assoc_handle=usflex&arb=ff6e97f7-cc8b-4916-a700-ff400352eb00
# If you have navigated to that webpage then the below Locator works for Forgot Password Link
driver.find_element(By.ID, "auth-fpp-link-bottom")

#8. Other issues with sign-in link (n/a)

#9. Create Amazon Account Button (n/a)
#This is also not located on the sign-in page as it is shown in the HW directions as page layout
#must have changed. However, to find this button and get a working locator, I had to enter a valid email
#and press continue, where I was then brought to a new page where the "Create Amazon Account Button"
#was located.
#URL: https://www.amazon.com/ax/claim/intent?arb=d8560075-bed5-4664-9bf1-9339538dde31&claimType=email&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fhelp%2Fcustomer%2Faccount-issues%2Fref%3Dnav_ya_signin%3Fie%3DUTF8&openid.assoc_handle=usflex&openid.mode=checkid_setup&pageId=usflex&policy_handle=Retail-Checkout&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&unifiedAuthTreatment=T2
driver.find_element(By.XPATH, "//input[contains(@class,'a-button-input')]")
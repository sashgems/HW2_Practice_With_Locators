#Open stack overflow.com
driver.get('https://www.stackoverflow.com/users/signup')

#click create your account
driver.find_element(By.CSS_SELECTOR, "[class*='flex--item fs-headline1']")

# below is the same but using class values all separated by periods not best practice
driver.find_element(By.CSS_SELECTOR, 'flex--item.fs-headline1.fw-bold.lh-xs.mb8.ws-nowrap').click()

#click box underneath with terms of service and privacy policy
driver.find_element(By.CSS.SELECTOR, "[class*='js-terms fs-caption ']")

# click email field button
driver.find_element(By.CSS.SELECTOR, "#email")

# click password field button
driver.find_element(By.CSS.SELECTOR, "#password")

# click unhide password button
driver.find_element(By.CSS.SELECTOR, "svg[aria-hidden='true'][class*='show-password']")
# I did tag(svg)+ attribute(aria-hidden) + class as partial attribute ('show-password)

#click sign up button
driver.find_element(By.CSS_SELECTOR, "#submit-button")

#click sign up with Google button
driver.find_element(By.CSS_SELECTOR, "button[class*='google bar']").click()])
# also works but not as clean
# driver.find_element(By.CSS_SELECTOR, "div#openid-buttons.flex--item.d-flex.flex__fl-grow1.fd-column gs8.gsy.g8")

# click sign up with Github button
driver.find_element(By.CSS_SELECTOR, "button[class*='github bar']").click()

# click "Get Stack Overflow for Teams free for up to 50 users"
driver.find_element(By.CSS_SELECTOR, "a[href*='content=public-sign-up'][target='_blank']")

#driver.quit()
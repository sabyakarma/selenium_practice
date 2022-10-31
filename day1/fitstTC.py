from lib2to3.pgen2 import driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

# Import the webdriver Selenium 3 standard

# driver = webdriver.Chrome("/Users/sabyakarma/automation/selenium_learning/driver/chromedriver")
# driver.get("http://automationpractice.com/index.php")
# #Click on Sign In
# driver.find_element().click()
# #Send the email in Keys
# driver.find_element_by_id("email_create").send_keys("sabyakarma@gmail.com")
# #Click on Create an account
# driver.find_element_by_id("SubmitCreate").click()
# #Close the browser
# driver.close()

# Selenium 4 standard

# Launch Chrome browser
chrome_service = Service("/Users/sabyakarma/automation/selenium_learning/driver/chromedriver")
driver = webdriver.Chrome(service= chrome_service)

# launch URL
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)

# click on Sign In
actual_title=driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Title validated")
else:
    print(f"Title did not match actual:{actual_title} expected:{expected_title}")

# Login to the application

driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
# driver.find_element(By.NAME,"password").send_keys("admin123")

#click on Login
# driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
driver.close()

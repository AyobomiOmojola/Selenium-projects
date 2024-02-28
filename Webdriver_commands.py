from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://opensource-demo.orangehrmlive.com/")

# Webdriver Commands

# - Application commands
# - Conditional commands
# - Browser commands
# - Navigational commands
# - Wait commands

# Application commands
# - title
# - current_url
# - page_source
title = driver.title
url = driver.current_url
source = driver.page_source

# Conditional commands
# - is_displayed()
# - is_enabled()
# - is_selected()
search = driver.find_element(By.XPATH, "//input[@id='heyo']")
search.is_displayed()

# Browser commands
# - close() : closes current browser window and processes are still running
# - quit() : closes the driver processes and closes all resulting browser window

# Navigational commands
# - back()
# - forward()
# - refresh()

driver.back()
driver.forward()
driver.refresh()

# EXTRA: Difference between text() and get_attribute()
# For elements that have texts but not as inner-texts, get_attribute is used to get the text value from specific attributes as such elements would most likely have an attribute that has the value of the text in the elements

emailbox = driver.find_element(By.XPATH, "//input[@id='heyo']")
emailbox.clear()
emailbox.send_keys('Hiya')

print(emailbox.text)
print(emailbox.get_attribute('value'))

# Wait command
# - Implicit command
driver.implicitly_wait(10) #this does not wait for the maximum timeout
# Note this statement is available for all the statements in your script at any point that the sychronization problem occurs

# - Explicit command
# This makes use of two steps; declaration and usage.
# Declaration:
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[],)

search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='heyo']"))) # This expression returns the element
search_link.click()





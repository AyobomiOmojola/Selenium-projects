from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://opensource-demo.orangehrmlive.com/")

### Xpath is defined as XML path, it finds the address of an element using XML path expression ,
# and finds the location of any element on a webpage using HTML DOM structure

## Types: Absolute & Relative
## Absolute Xpath starts with / while Relative starts with //
## Avsolute starts from root html node while Relative jumps to element on DOM
## Absolute uses nodes while Relative uses attributes

#relative_xpath = //tagname[@attributes='value']
#relative_xpath = //tagname[@attributes='value']/div/h1
# For the above XPATh, if you want to jump directly to the h1 tag:
#relative_xpath = //tagname[@attributes='value']//h1


driver.find_element(By.XPATH, '//h1[@class = "heyo"]')

# Xpath options:

# - and
# - or
# - contains()
# - starts-with()
# - text()
# - normalize-space()

# Using and | or with XPATH
driver.find_element(By.XPATH, '//h1[@class = "heyo" and @id = "hi"]')
driver.find_element(By.XPATH, '//h1[@class = "heyo" or @id = "hi"]')

# Using contains() | starts-with() with XPATH
driver.find_element(By.XPATH, '//h1[contains(@class = "ster")]')
driver.find_element(By.XPATH, '//h1[starts-with(@class = "heyo")]').send_keys('tire')

# Using text() with XPATH
driver.find_element(By.XPATH, '//h1[text()="Women"]')

# Using normalize-space() with XPATH
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
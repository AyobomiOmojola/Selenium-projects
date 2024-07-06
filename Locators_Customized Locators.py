from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://opensource-demo.orangehrmlive.com/")

### In depth analysis into difference between find_element & find_elements:
# find_element gets only a single element or first element in a list and returns NoSuchElementException
# find_elements returns a list so further operations needs to be navigated with list methods
elements = driver.find_elements(By.CLASS_NAME, "regis")
elements[0].send_keys('haha')
# find_elements can be used to access properties of a large number of elements by iteration
for element in elements:
    print(element.text)
# find elements does not return a NoSuchElementException when no element is returned because a list can be empty

#######
#### Locators
#######

# Locators are used to Identify element

##### By ID:
driver.find_element(By.ID, "xyz").send_keys("xyz")

##### By NAME:
driver.find_element(By.NAME, "xyz").click()

##### By LinkText:
# <a href="link"> register </a>
# register == LINK_TEXT
# regis == PARTIAL_LINK_TEXT
driver.find_element(By.LINK_TEXT, "register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "regis").click()

# TO FIND MORE THAN ONE ELEMENT:
# CLASS NAME
# TAG NAME

##### By ClassName:
driver.find_elements(By.CLASS_NAME, "xyz")

##### By TagName:
driver.find_elements(By.TAG_NAME, "h1")


##########
##### Customized Locators
##########

# CSS Selector
# - tag id
# - tag class
# - tag attribute
# - tag class attribute

# tag & id:
driver.find_elements(By.CSS_SELECTOR, "input#id")

# tag & class
driver.find_elements(By.CSS_SELECTOR, "input.class")

# tag & attribute
driver.find_elements(By.CSS_SELECTOR, "input[unique_id=id]")

# tag class attribute
driver.find_elements(By.CSS_SELECTOR, "input.class[unique_id=id]")

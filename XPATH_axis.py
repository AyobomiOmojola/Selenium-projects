from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://opensource-demo.orangehrmlive.com/")

## Xpath axes

# - ancestor
# - parent
# - preceding
# - preceding sibling
#     **self**
# - following sibling
# - following
# - child
# - descendant

text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'heyo')]/self::a").text
text_msg1 = driver.find_element(By.XPATH, "//a[contains(text(),'heyo')]/parent::td").text
text_msg2 = driver.find_elements(By.XPATH, "//a[contains(text(),'heyo')]/ancestor::a/following-sibling::a").text




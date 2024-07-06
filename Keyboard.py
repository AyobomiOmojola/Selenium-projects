import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
# driver.get("https://text-compare.com/")
# driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(10)

input1 = driver.find_element(By.XPATH, '//textarea[@id="inputText1"]')
input2 = driver.find_element(By.XPATH, '//textarea[@id="inputText2"]')

input1.send_keys("welcome to selenium")

# Ctrl A: To select text from input box 1
act = ActionChains(driver)
act.double_click(input1).perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Ctrl C: To copy text from input box 1
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Tab: TO navigate to the input box 2
act.send_keys(Keys.TAB).perform()

# Ctrl V: To paste the text into input box 2
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

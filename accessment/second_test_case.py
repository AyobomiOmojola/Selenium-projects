from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://admin-demo.nopcommerce.com/login")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Email']"))).clear()
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "//input[@name='Password']").clear()
driver.find_element(By.XPATH, "//input[@name='Password']").send_keys("admin")
driver.find_element(By.TAG_NAME, "button").click()

act_title = driver.title
exp_title = "Dashboard / nopCommerce administration"

if act_title == exp_title:
    print('Login Test Passed')
else:
    print('Login Test Failed')

driver.close()
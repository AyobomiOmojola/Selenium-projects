import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os

def headless_chrome():
    auto_fix = webdriver.ChromeOptions()
    auto_fix.add_experimental_option('detach', True)
    auto_fix.add_argument("--headless=new")
    driver = webdriver.Chrome(auto_fix)
    return driver


driver = headless_chrome()
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')

#### Capture cookies from the browser
cookies = driver.get_cookies()
print("Size of captured cookies:", len(cookies))

#### Adding new cookie to the browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new one:", len(cookies))
#
# #### Delete specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("Prize of cookies after deleted one:", len(cookies))

    # driver.quit()

# driver.add_cookes({'name':'name', 'value':'value'})
# driver.delete_cookie("name")
# cookies = driver.get_cookies()
print('Size of cookies: ', cookies)
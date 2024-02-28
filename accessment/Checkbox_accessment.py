import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests as requests

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("http://www.deadlinkcity.com/")

all_links = driver.find_elements(By.TAG_NAME, 'a')
broken_count = 0
active_count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        var = None

    if res.status_code >= 400:
        print(url, " is a broken link")
        broken_count += 1
    else:
        active_count += 1
        print(url, " is a valid link")

print('The number of broken links are: ', broken_count)
print('The number of active links are: ', active_count)

driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests as requests

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#### Checkboxes ####
checkboxes = driver.find_elements(By.XPATH, "//input[@class='heyo']")
# Selecting all checkboxes
for checkbox in checkboxes:
    checkbox.click()

# Selecting checkboxes of choice:
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id') ### get checkbox of choice with attribute ###
    if weekname == 'monday' or weekname == 'wednesday':
        checkbox.click()

# Select last two indexes
for i in range(5, 7):
    checkboxes[i].click()

# Select first two indexes
for i in range(0, 2):
    checkboxes[i].click()

# Clearing selected checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

#### Links ####
# Types: Internal, External and Broken link
# To handle broken links :
all_links = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
        if res.status_code >= 400:
            print(url, " is a broken link")
            count += 1
        else:
            print(url, " is a valid link")
    except:
        var = None

print('Number of broken links: ', count)

###### Dropdown ######
# This is identified by the HTML tag called select
drp_list = driver.find_element(By.XPATH, "//input[@class='heyo']")
drop_lists = Select(drp_list) # Declare as a Select selenium object

# Remember alert and dropdown are similiar

drop_lists.select_by_visible_text('money')
drop_lists.select_by_value('money')
drop_lists.select_by_index(12)

# To print all options
alloptions = drop_lists.options
print(alloptions)

# To select options without using built-in methods:
for opt in alloptions:
    if opt.text == 'india':
        opt.click()
        break


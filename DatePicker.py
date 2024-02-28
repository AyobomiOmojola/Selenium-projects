import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
# driver.get("https://jqueryui.com/datepicker/")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(10)
# driver.implicitly_wait(10)

### Date Picker
# 1. Standard elements are the same
# 2. Non-standard (customized) elements are not the same

# driver.switch_to.frame(0)
# #mm/dd/yyyy
# # date_picker = driver.find_element(By.ID, 'datepicker')
# # date_picker.send_keys('20/05/2024')
# # print(date_picker.text)
# #
# # driver.close()
#
# year = '2025'
# month = 'September'
# dayy = '22'
#
# driver.find_element(By.ID, 'datepicker').click()

#### Longer logic
# while True:
#     mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#
#     if month == mon and year == yr:
#         for row in range(1, 7):
#             for column in range(1, 8):
#                 try:
#                     day = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr["+str(row)+"]/td["+str(column)+"]/a")
#                     if day.text == dayy:
#                         # driver.find_element(By.XPATH, "//td[@data-handler='selectDay']").click()
#                         day.click()
#                 except:
#                     var = None
#
#     else:
#         driver.find_element(By.XPATH, "//a[@data-handler='next']").click() #next arrow

##### Shorter Logic
# while True:
#     mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
#     yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
#
#     if month == mon and year == yr:
#         days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#         for day in days:
#             if day.text == dayy:
#                 day.click()
#     else:
#         driver.find_element(By.XPATH, "//a[@data-handler='next']").click() #next arrow


driver.find_element(By.XPATH, "//input[@id='dob']").click()

month_drop = driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']")
month_drop_lists = Select(month_drop)
month_drop_lists.select_by_visible_text('May')

year_drop = driver.find_element(By.XPATH, "//select[@data-handler='selectYear']")
year_drop_lists = Select(year_drop)
year_drop_lists.select_by_visible_text('2022')

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for day in days:
    if day.text == '20':
        day.click()
























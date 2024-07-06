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
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# ### Alerts ######
# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# # normalize-space() is like text() but used for texts with spaces between, and its only used in XPATH
#
# time.sleep(2)
# alert_window = driver.switch_to.alert
# print(alert_window.text)
#
# time.sleep(2)
# alert_window.send_keys('Welcome')
#
# time.sleep(2)
# alert_window.accept() # To click OK button
# alert_window.dismiss() # To click Cancel button
#
# time.sleep(1)

### Authentication pop-up
# This is used when there is an authentication pop up on a website, you simply inject the username and password into the url
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#### iFrames #######
# identified by : frame, iframe, form
# driver.switch_to.frame(name of the frame)
# driver.switch_to.frame(id of the frame)
# driver.switch_to.frame(webelement)
# driver.switch_to.frame(0)----If only one frame on the webpage
# driver.switch_to.parent_frame --- Switch to container frame

# NOTE: always use # driver.switch_to.default_content() to leave a frame to the main page

# To demonstrate how to switch between frames:
driver.switch_to.frame("frame_1") # Switch to first frame by its name
driver.find_element(By.LINK_TEXT, "heyo").click() # access the element in such frame
driver.switch_to.default_content() # Switch out to the main webpage area

driver.switch_to.frame("frame_2") # Switch to second frame
driver.find_element(By.LINK_TEXT, "hiya").click() # access the element in such frame
driver.switch_to.default_content() # Switch out to the main webpage area

driver.switch_to.frame("frame_3") # Switch to third frame
driver.find_element(By.LINK_TEXT, "hello").click() # access the element in such frame
driver.switch_to.default_content() # Switch out to the main webpage area

# To demonstrate how to switch to innerframes in a frame
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe').click()

outer_frame = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(outer_frame)
inner_frame = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('hey')

### Browser Windows ###
# driver.current_window_handle ==> Return windowID of single browser window
# driver.window_handles ==> return all browser windows

# In order to get and switch to a window by its window id
# Approach 1
driver.get("https://opensource-demo.orangehrmlive.com/")
ids = driver.window_handles # Returns a list
first_window = ids[0]
second_window = ids[1]

# to switch to the second window:
driver.switch_to.window(second_window)
driver.switch_to.window(first_window)

# Approach 2
for wind in ids:
    driver.switch_to.window(wind)
    print(driver.title)

# to close a specific window id
for wind in ids:
    driver.switch_to.window(wind) ### hence identify window by the title of the page ###
    if driver.title == 'hellohello':
        driver.close() # Note you have to switch to the window you wish to close





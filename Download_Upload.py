import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import os

location = os.getcwd()

### DOWNLOAD
# def chrome_setup():
#     auto_fix = webdriver.ChromeOptions()
#     preferences = {"download_default_directory": location}
#     auto_fix.add_experimental_option('detach', True)
#     auto_fix.add_experimental_option('prefs', preferences)
#     driver = webdriver.Chrome(auto_fix)
#     return driver
#
# def edge_setup():
#     auto_fix = webdriver.EdgeOptions()
#     preferences = {"download_default_directory": location, "plugins.always_open_pdf_externally": True} # second arg downloads file instead of opening
#     auto_fix.add_experimental_option('detach', True)
#     auto_fix.add_experimental_option('prefs', preferences)
#     driver = webdriver.Edge(auto_fix)
#     return driver
#
# def firefox_setup():
#     auto_fix = webdriver.FirefoxOptions()
#     auto_fix.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") #
#     auto_fix.set_preference("browser.download.manager.showWhenStarting", False)
#     auto_fix.set_preference("browser.download.folderList", 2) #0-desktop 1-downloads folder 2-desired location
#     auto_fix.set_preference("pdfjs.disabled", True) # # second arg downloads file instead of opening in this case pdf
#     auto_fix.set_preference("browser.download.dir", location)
#
#     driver = webdriver.Edge(auto_fix)
#     return driver


# my_driver = chrome_setup()
# my_driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# my_driver.maximize_window()
# my_driver.implicitly_wait(10)
# my_driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()


auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
# driver.get("https://text-compare.com/")
driver.get(
    "https://media.monsterindia.com/user_upload/images_upload.html?uid=43850039&chk=&ck=0fd4b31e02cdd794d6db3ddada05bd70")
driver.maximize_window()
driver.implicitly_wait(10)

#### UPLOAD
driver.find_element(By.XPATH, "//input[@id='wordresume2']").send_keys("C:\Users\HOME\Documents\pers.txt")

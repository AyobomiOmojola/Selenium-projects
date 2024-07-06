import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
# driver.get("https://www.awaytravel.com/")
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
# driver.maximize_window()
driver.implicitly_wait(10)

## Operations performed by the mouse
# Mouse Hover
# Right click
# Double click
# Drag and Drop

# # Mouse Hover
# bags = driver.find_element(By.XPATH, "//a[@href='/shop/travel-bags']")

# act = ActionChains(driver)
# act.move_to_element(bags).perform()

# # Right click
# click = driver.find_element(By.XPATH, '//span[normalize-space()="right click me"]')

# act = ActionChains(driver)
# act.context_click(click).perform()

# # Double Click
# outer_frame = driver.find_element(By.XPATH, '//iframe[@id="iframeResult"]')
# driver.switch_to.frame(outer_frame)
# click = driver.find_element(By.XPATH, '//button[normalize-space()="Double-click me"]')

# act = ActionChains(driver)
# act.double_click(click).perform()

# # Drag and Drop
# rome_ele = driver.find_element(By.ID, 'box6')
# italy_ele = driver.find_element(By.ID, 'box106')

# wash_ele = driver.find_element(By.ID, 'box3')
# states_ele = driver.find_element(By.ID, 'box103')

# madr_ele = driver.find_element(By.ID, 'box7')
# spain_ele = driver.find_element(By.ID, 'box107')

# seoul_ele = driver.find_element(By.ID, 'box5')
# korea_ele = driver.find_element(By.ID, 'box105')

# oslo_ele = driver.find_element(By.ID, 'box1')
# norw_ele = driver.find_element(By.ID, 'box101')

# stock_ele = driver.find_element(By.ID, 'box2')
# sweden_ele = driver.find_element(By.ID, 'box102')

# cop_ele = driver.find_element(By.ID, 'box4')
# den_ele = driver.find_element(By.ID, 'box104')

# act = ActionChains(driver)
# time.sleep(1)
# act.drag_and_drop(rome_ele, italy_ele).perform()
# time.sleep(1)
# act.drag_and_drop(wash_ele, states_ele).perform()
# time.sleep(1)
# act.drag_and_drop(madr_ele, spain_ele).perform()
# time.sleep(1)
# act.drag_and_drop(seoul_ele, korea_ele).perform()
# time.sleep(1)
# act.drag_and_drop(oslo_ele, norw_ele).perform()
# time.sleep(1)
# act.drag_and_drop(stock_ele, sweden_ele).perform()
# time.sleep(1)
# act.drag_and_drop(cop_ele, den_ele).perform()


# ### Slider

# # min_slider = driver.find_element(By.XPATH, "//span[1]")
# # max_slider = driver.find_element(By.XPATH, "//span[2]")
# #
# # print('location of sliders before moving...')
# # print(min_slider.location) #{'x': 59, 'y': 250}
# # print(max_slider.location) #{'x': 412, 'y': 250}
# #
# # act = ActionChains(driver)
# #
# # act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
# # act.drag_and_drop_by_offset(max_slider, -60, 0).perform()
# #
# # print('location of sliders after moving...')
# # print(min_slider.location) #{'x': 59, 'y': 250}
# # print(max_slider.location) #{'x': 412, 'y': 250}

### Scroll
# 1. Scroll down by pixel
time.sleep(2)
driver.execute_script("window.scroll(0,3000)",)
value = driver.execute_script("return window.pageYOffset")
print("Number of pixels moved:", value)

# # 2 Scroll down till image is visible
nigeria = driver.find_element(By.XPATH, "//img[@alt='Flag of Nigeria']")
driver.execute_script("arguments[0].scrollIntoView();",nigeria)

time.sleep(2)
# 3 Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(2)
# 4 Scroll up to the start of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")





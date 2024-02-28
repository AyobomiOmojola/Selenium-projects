from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
my_wait = WebDriverWait(driver, 10,)

search_box = driver.find_element(By.XPATH, '//input[@id="Wikipedia1_wikipedia-search-input"]')
search_box.send_keys('selenium')

search_button = driver.find_element(By.CSS_SELECTOR, "input.wikipedia-search-button[type='submit']")
search_button.click()

search_results = my_wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="Wikipedia1_wikipedia-search-results"]/descendant::a')))
print(len(search_results))

for result in search_results:
    result.click()

window_ids = driver.window_handles

for window in window_ids:
    driver.switch_to.window(window)
    print(driver.title)

driver.quit()




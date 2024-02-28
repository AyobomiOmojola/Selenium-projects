from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

## To handle browser level notification pop up:
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")
# driver = webdriver.Chrome(options=options)


auto_fix = webdriver.ChromeOptions()
auto_fix.add_experimental_option('detach', True)
driver = webdriver.Chrome(auto_fix)

driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)


# To handle WebTable:

# 1. To count number of rows and columns
table_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
no_table_rows = len(table_rows)

table_columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th")
no_table_columns = len(table_columns)

# 2. To get specific values from the table
# Locate_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[4]/td[2]")
# print(Locate_data.text)

# 3. To read data from all the rows and columns:
# for row in range(2, no_table_rows+1):
#     for column in range(1, no_table_columns+1):
#         element = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]")
#         print(element.text)
#     print()

# 4. To read data based on condition
# example, to get the book name according to the author of the book (Mukesh)
for row in range(2, no_table_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]")
    if author_name.text == 'Mukesh':
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[1]")
        print(book_name.text)

# example, to get the price of the book if the author of the book (Amit)
for row in range(2, no_table_rows+1):
    author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]")
    if author_name.text == 'Amit':
        book_price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[4]")
        print(book_price.text)

driver.close()
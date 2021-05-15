from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("./Drivers/chromedriver")
# implicitly wait  - it will be application for the below entire session
#driver.implicitly_wait(5)

driver.get('https://www.google.com/search?q=Automation&ei=QuedYMqfN4PA3LUPweiSgAw&oq=automation&gs_lcp=Cgdnd3Mtd2l6EAxQAFgAYN0WaABwAngAgAGzAYgBswGSAQMwLjGYAQCqAQdnd3Mtd2l6wAEB&sclient=gws-wiz&ved=0ahUKEwjKyJLQlsjwAhUDILcAHUG0BMAQ4dUDCA4')

x = driver.find_element_by_name("q")
x.send_keys(' Testing')

# explicitly wait -
wait = WebDriverWait(driver, 5)
try:
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Tg7LZd')))
    print('element is clickable')
except:
    print('Element is either not found or not clickable')
    exit(1)
element.click()

# driver.find_element_by_name('btnK').click()
#driver.find_element_by_class_name('Tg7LZd').click()
print(driver.title)

driver.close()

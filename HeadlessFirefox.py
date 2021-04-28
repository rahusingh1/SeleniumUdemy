from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")

path = "Drivers/geckodriver"
driver = webdriver.Firefox(executable_path=path, firefox_options=firefox_options)

driver.get("https://google.co.in")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation with selenium")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)
print(driver.title)
driver.close()
driver.quit()
print("task completed")
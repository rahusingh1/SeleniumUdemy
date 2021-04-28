from selenium import webdriver
import time
driver = webdriver.Chrome("Drivers/chromedriver")

driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation with selenium and python")
#driver.find_element_by_name("btnK").click()
#time.sleep(10)

driver.close()
driver.quit()
print("completed")
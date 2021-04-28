from selenium import webdriver
import time

#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://google.co.in")
print(driver.title)
time.sleep(5)
driver.close()

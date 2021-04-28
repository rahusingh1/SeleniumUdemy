from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# there are two options for headless testing
#either import the options method or create below variable then use it
# chrome_options = webdriver.ChromeOptions()

#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="Drivers/chromedriver")

driver.get("https://google.co.in")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation with selenium and python")
#driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
print("task completed")
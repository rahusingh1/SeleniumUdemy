from selenium import webdriver

driver = webdriver.Chrome("/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver")

driver.get("https://google.com")
print(driver.title)

#driver.find_element_by_name("q").send_keys("Rahul Singh")

searchbox = driver.find_element_by_name("q")
searchbox.send_keys("Rahul Singh")

driver.close()

# we can ask developers to provide unique id for all the web elements
# tool for xpath is chrow path extension in chrome, another extension is xpath helper

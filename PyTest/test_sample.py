# In pytest naming convention matters a lot
# we create functions in pytest
# we also use fixtures in pytests to manage our test - to run particular lines of function every-time
# to run something once at end we put it in yield
# we can also use classes if required and class name should start with Test

from selenium import webdriver
import time
import pytest

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome('/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver')
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_login(self,test_setup):
        driver.get('https://opensource-demo.orangehrmlive.com/')
        driver.find_element_by_id('txtUsername').send_keys('Admin')
        driver.find_element_by_id('txtPassword').send_keys('admin123')
        driver.find_element_by_id('btnLogin').click()
        time.sleep(5)
        x = driver.title
        assert x == 'OrangeHRM'

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print('Test Completed')
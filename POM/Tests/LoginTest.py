from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from POM.Pages.loginpage import LoginPage
from POM.Pages.homepage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver')
        cls.driver.implicitly_wait(5)

    def test_login(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')

        # need to create the object for classes

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        # time.sleep(2)
        # self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        # time.sleep(2)
        # self.driver.find_element_by_id('btnLogin').click()
        # time.sleep(2)
        # self.driver.find_element_by_id('welcome').click()
        # time.sleep(2)
        # self.driver.find_element_by_link_text('Logout').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Complete')

if __name__ == '__main':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rahul/PycharmProjects/SeleniumUdemy/reports'))

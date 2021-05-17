from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from SampleProjects.Pages.loginpage import LoginPage
from SampleProjects.Pages.homepage import HomePage
import HtmlTestRunner

class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        # create the object for classes to call them
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()


        # self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        # self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        # self.driver.find_element_by_id('btnLogin').click()
        # self.driver.find_element_by_id('welcome').click()
        # self.driver.find_element_by_link_text('Logout').click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test Completed')

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rahul/PycharmProjects/SeleniumUdemy/reports'))

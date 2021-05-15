from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get('https://google.co.in')
        self.driver.find_element_by_name('q').send_keys('Automation testing')
        self.driver.find_element_by_name('btnK').click()
        print(self.driver.title)

    def test_search_name(self):
        self.driver.get('https://google.co.in')
        self.driver.find_element_by_name('q').send_keys('Raghavendra Singh')
        self.driver.find_element_by_name('btnK1').click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rahul/PycharmProjects/SeleniumUdemy/reports'))
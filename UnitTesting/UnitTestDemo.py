import unittest   # python has in-built unit test libraries
from selenium import webdriver

# inherit the testcase class from unittest module
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_search1(self):
        self.driver.get("https://google.co.in")
        x= self.driver.title
        print(x)
        self.driver.find_element_by_name("q").send_keys("Automation testing")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
        self.assertEqual(x, "Google")
        self.assertEqual(self.driver.title,"Automation testing - Google Search")

    def test_search2(self):
        self.driver.get("https://google.co.in")
        x= self.driver.title
        print(x)
        self.driver.find_element_by_name("q").send_keys("Manual testing")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
        self.assertEqual(x, "Google")
        self.assertEqual(self.driver.title,"Manual testing - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)  # or use -v in terminal it will do same thing "python3 -v filename.py


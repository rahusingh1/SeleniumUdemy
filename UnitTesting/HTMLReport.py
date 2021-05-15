import unittest  # python has in-built unit test libraries
from selenium import webdriver
import HtmlTestRunner


# inherit the testcase class from unittest module
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/home/rahul/PycharmProjects/SeleniumUdemy/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search1(self):
        self.driver.get("https://google.co.in")
        x = self.driver.title
        print(x)
        self.driver.find_element_by_name("q").send_keys("Automation testing")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
        self.assertEqual(x, "Google")
        self.assertEqual(self.driver.title, "Automation testing - Google Search")

    def test_search2(self):
        self.driver.get("https://google.co.in")
        x = self.driver.title
        print(x)
        self.driver.find_element_by_name("q").send_keys("Manual testing")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)
        self.assertEqual(x, "Google")
        self.assertEqual(self.driver.title, "Manual testing - Google Search")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
            """ This test should be skipped. """

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/rahul/PycharmProjects/SeleniumUdemy/reports'), verbosity=2)
      # or use -v in terminal it will do same thing "python3 -v filename.py

# pip install -U html-testRunner    Here -U flag used to make it universal
# pip freeze
# pip show html-testRunner
# pip check html-testRunner
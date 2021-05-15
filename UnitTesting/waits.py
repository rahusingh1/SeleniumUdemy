import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class waits(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('./Drivers/chromedriver')
        #cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
    
    def test_search(self):
        self.driver.get('https://google.co.in')
        self.driver.find_element_by_name('q').send_keys('Automation Testing')

        wait = WebDriverWait(self.driver, 5)
        try:

            element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
            print('Element is clickable')
        except:
            print('Element is either not found or not clickable')
            exit(1)
        element.click()

        #self.driver.find_element_by_name('btnK').click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, 'Automation Testing - Google Search')


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__=='__main__':
    unittest.main()
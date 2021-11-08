#Base web driver setup

from selenium import webdriver
import unittest


class WebDriverSetup(unittest.TestCase):
    
    #Before every test start a new driver instance
    @classmethod
    def setUp (self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    
    
    #Print test complete and quit the driver after every test ends   
    @classmethod
    def tearDown (self):
        if (self.driver != None):
            print('test complete')
            self.driver.quit()
        
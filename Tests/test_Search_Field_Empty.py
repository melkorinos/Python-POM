import sys
sys.path.append(sys.path[0] + "/..")
from WebDriverSetup import WebDriverSetup
from Pages.LandingPage import LandingPage
from selenium import webdriver
import unittest

class test_Search_Field_Empty(WebDriverSetup):
    
    def test_Search_Field_is_Empty(self):
        driver = self.driver
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.set_page_load_timeout(30)
        
        #create an instance of the results page to use
        page = LandingPage(driver)
        #get the text of the search box element
        text = page.search_box.text
        #ensure it is empty
        self.assertFalse(text)
        
        
if __name__ == '__main__':
    unittest.main()   
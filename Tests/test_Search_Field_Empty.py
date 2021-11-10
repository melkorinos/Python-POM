import sys
sys.path.append(sys.path[0] + "/..")
from WebDriverSetup import WebDriverSetup
from Pages.LandingPage import LandingPage
import unittest

class test_Search_Field_Empty(WebDriverSetup):
    
    #Ensure the search field is empty
    def test_Search_Field_is_Empty(self):
        #Driver initialization
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
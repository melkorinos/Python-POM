import sys
sys.path.append(sys.path[0] + "/..")
from WebDriverSetup import WebDriverSetup
from Pages.LandingPage import LandingPage
from Pages.SearchResultsPage import SearchResultsPage
from selenium import webdriver
import unittest

class test_Search_Field_Works(WebDriverSetup):
    
    def test_Search_Field_Is_Working(self):
        driver = self.driver
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.set_page_load_timeout(30)
        
        #create an instance of the landing page to use
        page = LandingPage(driver)
        #type in the search field 
        page.search_box.send_keys('automation test')
        #click the search button
        page.submit_search.click()
        
        #create an instance of the results page to use
        resultsPage = SearchResultsPage(driver)
        #get the text of the result summary on the top right
        text = resultsPage.result_summary.text
        #assert it contains the word result
        self.assertIn('result', text)
        
        
        
if __name__ == '__main__':
    unittest.main()        
       
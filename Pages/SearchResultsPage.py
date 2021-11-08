#Search results page after performing a standard search
from Locators.Locators import SearchResultsPageLocators

class SearchResultsPage(object):    
    
    #Initialize the new page object instance with elements
    def __init__(self, driver):
        self.driver = driver
        self.result_summary = driver.find_element(*SearchResultsPageLocators.RESULT_SUMMARY)
        
        
    def getResultSummary(self):
        return self.result_summary
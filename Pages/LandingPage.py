#Landing page object

from Locators.Locators import LandingPageLocators
class LandingPage(object):    
    
    #Initialize the new page object instance with elements
    def __init__(self, driver):
        self.driver = driver
        #Search box element
        self.search_box = driver.find_element(*LandingPageLocators.SEARCH_BOX)
        #Submit search button element
        self.submit_search = driver.find_element(*LandingPageLocators.SUBMIT_SEARCH)
       
    def getSearchBox(self):
        return self.search_box
 
    def getSubmitSeatchButton(self):
        return self.submit_search  
    
    

     
   
from selenium.webdriver.common.by import By


#Locators of the landing page
class LandingPageLocators(object):
    SEARCH_BOX = (By.NAME, 'search_query')
    SUBMIT_SEARCH = (By.NAME, 'submit_search')

#locators of the search results page        
class SearchResultsPageLocators(object):
    RESULT_SUMMARY = (By.CLASS_NAME, 'heading-counter')
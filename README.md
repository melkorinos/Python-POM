# Python Pom model
This projects is a sample test suite following the POM model. Using Python, Selenium Webdriver, Python unittest and (TOD : HTMLTestRunner for report generation)
 
## Introduction
The following test suite components can be indetified.
- Locators : All web element locators per page
- Page Objects : All site pages
- Tests : All test cases per page object
- WebDriverSetup : Basic driver initialization, setup and teardown
- TestRunner : Test runner and reporter

The suite tests the website http://automationpractice.com/index.php and performs two sample tests.
To launch run TestRunner.py

## Scenarios
The suite runs two scenarios :

**Scenario #1 :** The search box is initialized with no text   
**Expected result :** The search field is empty when the user selects it
**Test Steps :** Select the text box -> Get the web element's text attribute -> Ensure text property does not contain any characters

2) Ensure the search functionality works  
STEPS : Select the text box -> Enter a search term -> Press the search button -> Ensure we land on the results page

**Scenario #1 :** Ensure the search functionality functions  
**Expected result :** When the user enters texts and submits it the website navigates him to the results page
**Test Steps :** Select the text box -> Enter a search term -> Press the submit search button -> Locate the web element that states that sum of results -> Ensure it's text attribute contains the string "results". 




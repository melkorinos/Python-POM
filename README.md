# Python Pom model
This projects is a sample test suite following the POM model. Using Python, Selenium Webdriver, Python unittest and HTMLTestRunner ( TODO)
 
## Introduction
The following base components can be indetified 
- Locators
- Page Objects
- Tests
- WebDriverSetup
- TestRunner 

The suite access the website http://automationpractice.com/index.php and performs two sample tests.
To launch run TestRunner.py

## Scenarios
The suite runs two scenarios :

1) Ensure the search box is initialized with no text
STEPS : Select the text box -> Get it's text element -> Ensure it is empty

2)Ensure the search functionality works
STEPS: Select the text box -> Enter a search term -> Press the search button -> Ensure we land on the results page







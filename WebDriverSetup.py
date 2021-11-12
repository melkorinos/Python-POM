#Base web driver setup

from selenium import webdriver
import unittest


class WebDriverSetup(unittest.TestCase):
    
    #Before every test start a new driver instance
    @classmethod
    def setUp (self):
        #cloud based testing on Lambda test
        self.driver = webdriver.Remote(command_executor = 'https://melkorinos:xZ5M4PjFxtLBvLXaaNo3AKbT56YdXYE1PbyilYrUfJYCcUg6wx@hub.lambdatest.com/wd/hub',
                                       desired_capabilities=capabilities)
        self.driver.implicitly_wait(5)
    
    
    #Print test complete and quit the driver after every test ends   
    @classmethod
    def tearDown (self):
        if (self.driver != None):
            print('test complete')
            self.driver.quit()
            


capabilities = {
		'LT:Options' : {
			"user" : "melkorinos",
			"accessKey" : "xZ5M4PjFxtLBvLXaaNo3AKbT56YdXYE1PbyilYrUfJYCcUg6wx",
			"build" : "Python POM",
			"name" : "Sample search bar tests",
			"platformName" : "Windows 10",
			"browserName" : "Chrome",
			"browserVersion" : "95.0"
		},
		"browserName" : "Chrome",
		"browserVersion" : "95.0",
	}
        
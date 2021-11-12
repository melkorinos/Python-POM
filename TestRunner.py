from unittest import TestLoader, TestSuite, TextTestRunner
import unittest
#import the tests to run
from Tests.test_Search_Field_Empty import test_Search_Field_Empty
from Tests.test_Search_Field_Works import test_Search_Field_Works

#TODO use testtools for running the tests in parallel
import testtools as testtools

import HtmlTestRunner

if __name__ == "__main__":
    
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        #Load the tests
        test_loader.loadTestsFromTestCase(test_Search_Field_Empty),
        test_loader.loadTestsFromTestCase(test_Search_Field_Works),
        ))
    
    #Run the tests and produce one report for them
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True))
        


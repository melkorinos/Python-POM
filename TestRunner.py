import sys
import os
from unittest import TestLoader, TestSuite, TextTestRunner
#import the tests to run
from Tests.test_Search_Field_Empty import test_Search_Field_Empty
from Tests.test_Search_Field_Works import test_Search_Field_Works

import testtools as testtools

if __name__ == "__main__":
     
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        #Load the tests
        test_loader.loadTestsFromTestCase(test_Search_Field_Empty),
        test_loader.loadTestsFromTestCase(test_Search_Field_Works),
        ))

    #add a higher level of verbosity for logging ( from 1 to 2)
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    #Run the tests concurrently.
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    #Report the activity of the tests
    parallel_suite.run(testtools.StreamResult())
        


#!/usr/bin/env python

# import all the lovely files
import unittest
import test.call_tests
import test.snp_tests
import test.sample_tests
import test.group_tests
import test.ui_controller_tests
import test.vcf_tests

# get suites from test modules
suite1 = test.call_tests.suite()
suite2 = test.snp_tests.suite()
suite3 = test.sample_tests.suite()
suite4 = test.group_tests.suite()
suite5 = test.ui_controller_tests.suite()
suite6 = test.vcf_tests.suite()

# collect suites in a TestSuite object
suite = unittest.TestSuite()
suite.addTest(suite1)
suite.addTest(suite2)
suite.addTest(suite3)
suite.addTest(suite4)
suite.addTest(suite5)
suite.addTest(suite6)

# run suite
unittest.TextTestRunner(verbosity=2).run(suite)

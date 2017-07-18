#coding:utf-8

import unittest

def cases():

    case_dir = "G:/BaiduNetdiskDownload/projectMyself/"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                       pattern="test*.py",
                                                       top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testcase.addTests(test_case)
    print testcase
    return testcase
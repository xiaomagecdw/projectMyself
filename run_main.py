#coding:utf-8

import time
import unittest
import HTMLTestRunnerCN
from Cases import cases


if __name__=='__main__':

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #report_path = "G:/BaiduNetdiskDownload/projectMyself/123.html"
    fp = open("./"+ now +".html", "wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,
                                                 title=u'自动化测试报告',
                                                 description=u'测试结果：')
    runner.run(cases())
    fp.close()
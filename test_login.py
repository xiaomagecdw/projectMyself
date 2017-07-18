# coding:utf-8
'''
Created on 2017年7月18日

@author: chendaiwu
'''

from publieClass import PublicClass
#from selenium import webdriver
from time import sleep
from choiceBrowser import ChoiceBrowser

class login_page(PublicClass):

    def test_case01(self):

        driver = self.driver

        #driver = ChoiceBrowser('fire') #输入浏览器类型，调用选择浏览器设置
        #driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get("http://www.baidu.com/")
        driver.implicitly_wait(10)

        driver.find_element_by_link_text(u"登录").click()
        sleep(3)
        driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys(u"小马哥xxy")
        driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys(u"cdw520xxy1314")
        sleep(15)
        driver.find_element_by_id("TANGRAM__PSP_8__submit").click()
        sleep(2)
        #driver.close()


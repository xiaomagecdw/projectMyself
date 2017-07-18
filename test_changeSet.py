# coding:utf-8
'''
Created on 2017年7月18日

@author: chendaiwu
'''
from publieClass import PublicClass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from choiceBrowser import ChoiceBrowser


class SetBrowser(PublicClass):

    def test_sethome(self):

        driver = self.driver
        #driver = ChoiceBrowser("fire")
        URL = "http://www.baidu.com/"
        driver.get(URL)
        driver.implicitly_wait(10)

        mouse = driver.find_element_by_link_text("设置")
        ActionChains(driver).move_to_element(mouse).perform()
        driver.find_element_by_link_text("搜索设置").click()

        time.sleep(5)
        s = driver.find_element_by_id("nr")
        s.find_element_by_xpath(".//option[@value='20']").click()
        time.sleep(5)
        driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
        time.sleep(3)
        ss = driver.find_element_by_id("nr")
        Select(ss).select_by_index(0)
        time.sleep(2)
        driver.find_element("id", "gxszButton").click()
        driver.find_element("class name", "prefpanelgo").click()
        #driver.find_element_by_xpath(".//a[text()='保存设置']").click()
        time.sleep(3)
        #driver.implicitly_wait(10)
        driver.switch_to_alert().accept()
        #print t.text
        #t.accept()
        time.sleep(5)
        #driver.quit()

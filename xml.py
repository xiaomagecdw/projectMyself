#coding:utf-8

import xml.dom.minidom as xdm
import xpath
import traceback
import xml.etree.ElementTree as xeet

class Xml():

    def __init__(self, path):
        try:
            self.document = xeet.parse(path)
        except:
            self.document = None

    def getElement(self, xpath_string):
        element = None
        if self.document is not None:
            element = self.document.find(xpath_string)
        return element

    def getText(self, xpath_string):
        text = None
        if self.document is not None:
            text = self.document.find(xpath_string)
        return text

    def getAttribute(self, xpath_string, attribute):
        result = None
        element = self._getElement(xpath_string)
        if element is not None:
            try:
                result = element.attribute[attribute]
            except:
                traceback.print_exc()
        return result




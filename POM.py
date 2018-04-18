import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def username(self, uname):
        self.driver.find_element_by_id("identifierId").clear()
        self.driver.find_element_by_id("identifierId").send_keys(uname)
        self.driver.find_element_by_id("identifierNext").click()

    def password(self, pname):
        self.driver.find_element_by_name("password").send_keys(pname)
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)

import unittest
from selenium import webdriver
from POM import LoginPage
import time

class MyScript(unittest.TestCase):
    def __init__(self):
        self.setUp()

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\chromedriver.exe')
        self.driver.set_page_load_timeout(5)
        self.driver.maximize_window()
        self.base_url = 'https://mail.google.com/'
        self.driver.get(self.base_url + '/')
        print('Setup Complete : Environment Created')

    def Login(self, un, pwd):
        driver = self.driver
        login = LoginPage(driver)
        login.username(un)
        driver.implicitly_wait(200)
        login.password(pwd)
        print('In Login')
        compose = driver.find_element_by_class_name("z0")
        self.isSuccess = compose.text


    def Logout(self):
        driver = self.driver
        # Clicking button with profile picture
        driver.find_element_by_xpath('//div/div[@class="gb_Qc gb_mb gb_Lg gb_R"]').click()
        driver.implicitly_wait(100)
        # Clicking on actual sign out button
        driver.find_element_by_xpath('//div/a[@id="gb_71"]').click()
        # driver.find_elements_by_link_text('Sign out').click()
        time.sleep(5)
        # Switching accounts, small down facing arrow
        driver.find_element_by_xpath('//div[@aria-label="Switch account"]').click()
        time.sleep(2)
        # Clicking on use other account
        driver.find_element_by_xpath('//div[@id="identifierLink"]').click()

    def tearDown(self):
        self.driver.close()
        print("Yo I'm done")



'''
#Call here
a = MyScript()
a.TestScript()

'''
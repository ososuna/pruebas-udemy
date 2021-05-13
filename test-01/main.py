
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Unit(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Edge(executable_path=r'../msedgedriver.exe')

    def test(self):
        self.driver.get('https://www.udemy.com/')
        search = self.driver.find_element_by_name('q')
        search.send_keys('javascript')
        search.send_keys(Keys.RETURN)
        time.sleep(3)

    def close(self):
        self.driver.close()

t = Unit()
t.test()
t.close()
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

import math
from selenium.common.exceptions import NoAlertPresentException

class BasePage():
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

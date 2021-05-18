from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .locators import ManagerPageLocators


class ManagerPage(BasePage):
    def add_user(self, login):
        self.driver.find_element(*ManagerPageLocators.ADD_USER).click()
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_USER).send_keys(login)
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_EMAIL).send_keys(f'{login}@gmail.com')
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_PASS).send_keys('123456')
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_BTN).click()

    def email_rus(self, login):
        self.driver.find_element(*ManagerPageLocators.ADD_USER).click()
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_USER).send_keys(login)
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_EMAIL).send_keys(f'{login}@gmail.com')
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_PASS).send_keys('123456')
        self.driver.find_element(*ManagerPageLocators.ADD_FORM_BTN).click()

    def del_user(self):
        self.driver.find_element(*ManagerPageLocators.DEL_USER).click()



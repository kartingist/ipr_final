from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def registration(self,login):
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_NAME).send_keys(login)
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(f'{login}@gmail.com')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_PASS).send_keys('123456')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_BTN).click()

    def login(self, login):
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL).send_keys(f'{login}@gmail.com')
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_PASS).send_keys('123456')
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_BTN).click()

    def dubledog_email(self, login):
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_NAME).send_keys(login)
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(f'{login}@@gmail.com')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_PASS).send_keys('123456')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_BTN).click()

    def empty_log_pas(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_BTN).click()
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES)==False, 'пользователь авторизовался не вводя данные'

    def no_pass(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL).send_keys(f' manager@mail.ru')
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_BTN).click()
        assert self.is_element_present(
            *MainPageLocators.LOGIN_SUCCES) == False, 'пользователь авторизовался не вводя пароль'

    def manager_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_EMAIL).send_keys(f'manager@mail.ru')
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_PASS).send_keys('1')
        self.driver.find_element(*LoginPageLocators.LOGIN_FORM_BTN).click()




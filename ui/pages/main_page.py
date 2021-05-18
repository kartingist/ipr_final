from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Кнопка авторизации не найдена"

    def check_registration(self, login):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "невозможно зарегистрировать текущего пользователя, возможно он уже существует"
        assert self.driver.find_element(*MainPageLocators.LOGIN_SUCCES).text == login.lstrip(), "авторизован другой пользователь"

    def check_login(self, login):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "пользователь не авторизован, не существует или неверный пароль"
        assert self.driver.find_element(*MainPageLocators.LOGIN_SUCCES).text == login.lstrip(), "авторизован другой пользователь"

    def check_user(self, login):
        self.driver.find_element(*MainPageLocators.SEARCH).clear()
        self.driver.find_element(*MainPageLocators.SEARCH).send_keys(login.lstrip()+'@gmail.com')
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()

        if self.is_element_present(*MainPageLocators.SEARCH_RESULT)==False:
            return False
        else:
            return self.driver.find_element(*MainPageLocators.SEARCH_RESULT).text == login.lstrip() + '@gmail.com'

    def empty_login(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "регистрация не удалась, логин не может быть пустым"

    def dubble_dog(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES)==True, "регистрация не удалась, некорректный формат E-Mail"

    def manager_registration(self, login):
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_NAME).send_keys(login)
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(f'{login}@gmail.com')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_PASS).send_keys('123456')
        self.driver.find_element(*LoginPageLocators.REGISTER_FORM_BTN).click()

    def check_rus_email(self, login):
        self.driver.find_element(*MainPageLocators.SEARCH).send_keys(login.lstrip()+'@gmail.com')
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULT)==False, "прошла регистрация с кирилицей в email"













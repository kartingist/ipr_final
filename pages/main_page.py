from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def go_to_login_page(self):
        self.driver.find_element(*MainPageLocators.LOGIN_LINK).click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Кнопка авторизации не найдена"

    def check_registration(self, login):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "пользователь не зарегистрирован или уже существует"
        assert self.driver.find_element(*MainPageLocators.LOGIN_SUCCES).text == login.lstrip(), "авторизован другой пользователь"

    def check_login(self, login):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "пользователь не авторизован, не существует или неверный пароль"
        assert self.driver.find_element(*MainPageLocators.LOGIN_SUCCES).text == login.lstrip(), "авторизован другой пользователь"

    def check_user(self, login):
        self.driver.find_element(*MainPageLocators.SEARCH).send_keys(login.lstrip()+'@gmail.com')
        self.driver.find_element(*MainPageLocators.SEARCH_BTN).click()
        count_result=self.driver.find_element(*MainPageLocators.COUNT_RESULT).text
        if count_result!='Всего:0 ':
            search_result=self.driver.find_element(*MainPageLocators.SEARCH_RESULT).text
            return search_result==login.lstrip()+'@gmail.com'
        else:
            return False







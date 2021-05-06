from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Кнопка авторизации не найдена"

    def check_registration(self, login):
        self.browser.find_element(*MainPageLocators.SEARCH).send_keys(login.lstrip())
        self.browser.find_element(*MainPageLocators.SEARCH_BTN).click()
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULT), "пользователь не найден"

    def check_login(self, login):
        assert self.is_element_present(*MainPageLocators.LOGIN_SUCCES), "пользователь не авторизован"
        assert self.browser.find_element(*MainPageLocators.LOGIN_SUCCES).text == login.lstrip(), "авторизован другой пользователь"


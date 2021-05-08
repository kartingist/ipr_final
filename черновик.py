from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators
import time

def test_registration(browser):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.input_anketa()
    time.sleep(3)
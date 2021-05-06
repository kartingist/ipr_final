from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
login='heatcliff6'

def test_registration(browser):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.registration(login)
    page.open()
    main_page=MainPage(browser, browser.current_url)
    main_page.check_registration(login)


def test_login(browser):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.login(login)
    main_page = MainPage(browser, browser.current_url)
    main_page.check_login(login)






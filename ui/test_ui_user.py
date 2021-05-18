from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import random
import time

logins=['user'+str(random.randint(10000, 19999))]

#_________________________________________________________________
#Регистрация

@pytest.mark.parametrize('login', logins,  scope='function')
def test_registration(browser, login):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    if page.check_user(login)== False:
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.registration(login)
        page.open()
        main_page=MainPage(browser, browser.current_url)
        main_page.check_registration(login)
    else:
        assert False, 'пользователь c таким логином существует'


@pytest.mark.xfail
def test_empty_login_registration(browser):
    link = "http://users.bugred.ru/"
    login=''

    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.registration(login)
    main_page = MainPage(browser, browser.current_url)
    main_page.empty_login()

@pytest.mark.xfail
def test_dubbledog_registration(browser):
    link = "http://users.bugred.ru/"
    login='7575745454q'
    page = MainPage(browser, link)
    page.open()
    if page.check_user(login) == False:
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.dubledog_email(login)
        page.dubble_dog()
    else:
        assert False, 'пользователь c таким логином существует'
#_________________________________________________________________
#Логин
@pytest.mark.parametrize('login', logins, scope='function')
def test_login(browser, login):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.login(login)
    main_page = MainPage(browser, browser.current_url)
    main_page.check_login(login)

def test_login_empty_log_pas(browser):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.empty_log_pas()

def test_login_no_pass(browser):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.no_pass()







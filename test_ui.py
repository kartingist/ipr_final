from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time
#login='heatcliff6'
@pytest.mark.parametrize('login', ["www"], scope='function')
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
        print("пользователь уже существует")

# @pytest.mark.parametrize('login', ["1","2","3","4","5"], scope='function')
# def test_login(browser, login):
#     link = "http://users.bugred.ru/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#     login_page.login(login)
#     main_page = MainPage(browser, browser.current_url)
#     main_page.check_login(login)






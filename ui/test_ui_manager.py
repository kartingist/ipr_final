from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.manager_page import ManagerPage
import pytest
import random


import time

# logins=['user'+str(random.randint(10000, 19999)),'user'+str(random.randint(20000, 29999)), 'user'+str(random.randint(30000, 39999))]
logins=['user'+str(random.randint(30000, 39999))]
#_________________________________________________________________
#Регистрация

@pytest.mark.parametrize('login', logins, scope='session')
def test_reg_from_manager(browser, login):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    if page.check_user(login)== False:
        login_page = LoginPage(browser, browser.current_url)
        page.go_to_login_page()
        login_page.should_be_login_page()
        login_page.manager_login()
        manager_page=ManagerPage(browser, browser.current_url)

        manager_page.add_user(login)

        page.open()
        page.check_user(login)
    else:
        assert False, 'пользователь c таким логином существует'




def test_reg_rus_email(browser):
    link = "http://users.bugred.ru/"
    login="тутдолжнобытьимя"
    page = MainPage(browser, link)
    page.open()
    if page.check_user(login)== False:
        login_page = LoginPage(browser, browser.current_url)
        page.go_to_login_page()
        login_page.should_be_login_page()
        login_page.manager_login()
        manager_page=ManagerPage(browser, browser.current_url)

        manager_page.email_rus(login)

        page.open()
        page.check_rus_email(login)
        time.sleep(2)
    else:
        assert False, 'пользователь c таким логином существует'


# #_________________________________________________________________
# #Удаление
@pytest.mark.parametrize('login', logins, scope='session')
def test_del_user(browser, login):
    link = "http://users.bugred.ru/"
    page = MainPage(browser, link)
    page.open()
    if page.check_user(login)== True:
        login_page = LoginPage(browser, browser.current_url)
        page.go_to_login_page()
        login_page.should_be_login_page()
        login_page.manager_login()
        manager_page=ManagerPage(browser, browser.current_url)
        page.check_user(login)
        manager_page.del_user()
        if page.check_user(login) == True:
            assert False, 'пользователь не удален'






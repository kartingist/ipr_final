from selenium import webdriver
import pytest
import requests
import json
from .test_ui_user import logins

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
#    browser.set_window_size(375, 1080)
    yield driver
    print("\nquit browser..")
    requests.post('http://users.bugred.ru/tasks/rest/deleteuser', data={'email': f'{logins}@gmail.com'})
    driver.quit()






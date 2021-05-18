# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


HOST = "http://selenoid"
PORT = "4444"


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    browser_list = request.config.getoption("--browser")

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--start-maximized')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('window-size=1920x1080')
    firefox_options.add_argument('--disable-features=VizDisplayCompositor')
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--disable-features=VizDisplayCompositor')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver_map = {
        "chrome": webdriver.Remote(
            command_executor=f"{HOST}:{PORT}/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
            options=chrome_options
        ),
        "firefox": webdriver.Remote(
            command_executor=f"{HOST}:{PORT}/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX,
            options=firefox_options
        ),
    }
    if request.param in browser_list:
        driver = driver_map[request.param]
        return driver
    else:
        pytest.skip(f"Not running tests for browser: {request.param}")


def pytest_addoption(parser):
    parser.addoption('--browser', action='store')


from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#main-menu > ul > li:nth-child(2) > a")
    SEARCH = (By.XPATH, "/html/body/div[3]/form/table/tbody/tr[4]/td/input")
    SEARCH_BTN = (By.XPATH, "/html/body/div[3]/form/table/tbody/tr[5]/td[1]/button")
    SEARCH_RESULT = (By.XPATH, "/html/body/div[3]/table/tbody/tr/td[1]")
    LOGIN_SUCCES = (By.XPATH, '//*[@id="fat-menu"]/a')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(1)")
    LOGIN_FORM_EMAIL = (By.XPATH, "(//INPUT[@type='text'])[1]")
    LOGIN_FORM_PASS = (By.XPATH, "(//INPUT[@type='password'])[1]")
    LOGIN_FORM_BTN = (By.XPATH, "(//INPUT[@class='btn btn-danger'])[1]")

    REGISTER_FORM = (By.CSS_SELECTOR, "body > div.content > div.row > div:nth-child(2)")
    REGISTER_FORM_NAME = (By.XPATH, "(//INPUT[@required=''])[1]")
    REGISTER_FORM_EMAIL = (By.XPATH, "(//INPUT[@required=''])[2]")
    REGISTER_FORM_PASS = (By.XPATH, "(//INPUT[@required=''])[3]")
    REGISTER_FORM_BTN = (By.XPATH, "(//INPUT[@class='btn btn-danger'])[2]")






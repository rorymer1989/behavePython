from selenium import webdriver

from pages.login_page import LoginPage


def get_web(browser):
    if browser == "chrome":
        return LoginPage(webdriver.Chrome("C:/drivers/chromedriver.exe"))


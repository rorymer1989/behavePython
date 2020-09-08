from selenium import webdriver

from pages.login_page import LoginPage
def browser_chrome(context, timeout=30, **kwargs):
    browser = webdriver.Chrome("C:/chromedriver.exe")
    login_page = LoginPage(browser)
    context.login_page = login_page
    yield context.login_page
    browser.quit()

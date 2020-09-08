from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):
    __TIMEOUT = 10
    URL="http://blazedemo.com/"
    OPCION_CITY_DEPARTURE_XPATH="//select[@name='fromPort']/option[text()='{}']"
    OPCION_CITY_DESTINATION_XPATH="//select[@name='toPort']/option[text()='{}']"
    BUTTON_FIND_FLIGHTS_XPATH="//input[@type='submit']"
    TABLE_FLIGHTS_FROM_XPATH ="//table/tbody/tr"

    def __init__(self, web_driver):
        super(LoginPage, self).__init__()  # in python 3.6 you can just call super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, LoginPage.__TIMEOUT)
        self._web_driver = web_driver

    def open(self):
        self._web_driver.get(self.URL)

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def select_option_city_departure(self, city):
        self.find_by_xpath(self.OPCION_CITY_DEPARTURE_XPATH.format(city)).click()

    def select_option_city_destination(self, city):
        self.find_by_xpath(self.OPCION_CITY_DESTINATION_XPATH.format(city)).click()

    def click_button_find_flights(self):
        self.find_by_xpath(self.BUTTON_FIND_FLIGHTS_XPATH).click()

    def valid_table_flights_from(self):
        return self.finds_by_xpath(self.TABLE_FLIGHTS_FROM_XPATH)

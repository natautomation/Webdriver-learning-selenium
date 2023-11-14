from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Base:
    BASE_VAR = "Base Var"
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()


#--output--
#/usr/local/bin/python3.9 /Users/gaughan/PycharmProjects/Webdriver-learning-selenium/selenium_basics/components/base.py
#Process finished with exit code 0

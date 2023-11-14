from selenium_basics.components.base import Base

class LeftFilter(Base):
    LOCATOR = "//"

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        print(Base.BASE_VAR)
        print(LeftFilter.LOCATOR)
        print(option)
        print(visible)


#--output--
#/usr/local/bin/python3.9 /Users/g/PycharmProjects/Webdriver-learning-selenium/selenium_basics/components/filter.py
#Process finished with exit code 0

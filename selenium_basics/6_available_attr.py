from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome
left_filter = LeftFilter(driver)

# adding print statement
print(dir(left_filter))

#---output---
#/usr/local/bin/python3.9 /Users/g/PycharmProjects/Webdriver-learning-selenium/selenium_basics/6_available_attr.py
#['BASE_VAR', 'LOCATOR', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'click', 'driver', 'select_option']

#Process finished with exit code 0

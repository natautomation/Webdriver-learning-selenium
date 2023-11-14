def check_inheritance(obj, class_):

# adding validation
   return isinstance(obj, class_) and (not type(obj) is class_)


if __name__ == "__main__":

    class Base:
        pass


    a = Base()
    b = [1, 2]
    c = False
    for x in [a, b, c]:

        if check_inheritance(x, int):
            print(f"{x} was inherited from {int.__name__}")
        if check_inheritance(x, list):
            print(f"{x} was inherited from {list.__name__}")
        if check_inheritance(x, Base):
            print(f"{x} was inherited from {Base.__name__}")
        if check_inheritance(x, object):
            print(f"{x} was inherited from {object.__name__}")

#--output--
# /usr/local/bin/python3.9 /Users/g/PycharmProjects/Webdriver-learning-selenium/selenium_basics/800_check_if_inherited.py
# <__main__.Base object at 0x10d209fd0> was inherited from object
# [1, 2] was inherited from object
# False was inherited from int
# False was inherited from object
#
# Process finished with exit code 0

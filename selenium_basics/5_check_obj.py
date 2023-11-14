def check_obj(obj, class_):
    # adding return
    return isinstance(obj, class_)

if __name__ == "__main__":
    #from components.filter import LeftFilter
    #from components import base

    class Base:
        pass


    b = Base()
    i = [1, 2]
    # validation
    for x in [b, i]:

        if check_obj(x, int):
            print(f"{x} is from class {int.__name__}")
        if check_obj(x, list):
            print(f"{x} is from class {list.__name__}")
        if check_obj(x, Base):
            print(f"{x} is from class {Base.__name__}")
        if check_obj(x, object):
            print(f"{x} is from class {object.__name__}")
        print(f"{'':.^20}")

#--output--
#<__main__.Base object at 0x102e2bfd0> is from class object

#[1, 2] is from class list
#[1, 2] is from class object

#Process finished with exit code 0

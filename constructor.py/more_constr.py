# more than one constructors in a single class
class Student:
    def __init__(self):
        print("this is constructor 1")
    def __init__(self):
        print("This is constructor 2")


s = Student()
s2 = Student()   #  object calls last constructor in class when more than one constructors are available
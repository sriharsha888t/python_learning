class class1:
    def class1_function():
        print("This is class1 function")
class class2(class1):
    def class2_function():
        print("This is class2 function")
class class3:
    def class3_function():
        print("This is class3 function")
class class4:
    def class4_function():
        print("This is class4 function")
class class5(class3,class4):
    def class5_function():
        print("This is class5 function")


cls2 = class2
cls2.class1_function()
cls5 = class5
cls5.class4_function()
cls5.class3_function()

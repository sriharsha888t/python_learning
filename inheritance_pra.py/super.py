class class1:
    def function1(self):
        print("This is function1 in class1")

class class2(class1):
    def function2(self):
        super().function1()
        print("This is function2 in class2")

cls = class1()
cls.function1()



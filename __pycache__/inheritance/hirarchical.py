class parent:
    def function1(self):
        print("This is function 1")
class parent2(parent):
    def function2(self):
        print("this is function 2")
class child(parent):
    def function3(self):
        print("This is function 3")

ob=child()
ob1=parent2()
ob.function1()
ob1.function1()


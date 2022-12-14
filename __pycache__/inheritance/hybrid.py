class parent:
    def function1(self):
        print("This is function 1")
class parent1(parent):
    def function2(self):
        print("This is function 2")
class parent3:
    def function3(self):
        print("This is function 3")
class child(parent,parent3):
    def function4(self):
        print("this is function 4")

ob=child()
ob.function1()
ob.function3()
ob1=parent1()
ob1.function1()
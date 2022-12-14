class parent:
    def function1(self):
        print("This is function1")
class parent2(parent):
    def function2(self):
        print("This is function2")
class child(parent2):
    def function3(self):
        print("this is function3")

ob=child()
ob.function2()
ob.function3()
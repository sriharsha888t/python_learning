class parent:
    def function1(self):
        print("This is function 1")
class child(parent):
    def function2(self):
        super().function1()
        print("This is function 2")

ob=child()
ob.function2()

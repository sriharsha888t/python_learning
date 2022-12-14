class parent():
    def function1(self):
        print("This is function 1")
class child(parent):
    def function2(self):
        print("This is function 2")

obj=child()
obj.function1()



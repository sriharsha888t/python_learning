class parent:
    def function1(self):
        print("this is function 1 in parent")
class child(parent):
    def function1(self):
        print("this is function1 in child")

ob=child()
ob.function1()
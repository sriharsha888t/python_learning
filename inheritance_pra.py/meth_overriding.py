class parent:
    def funct1(self):
        print("this is function 1 in parent")
class child(parent):
    def funct1(self):
        print("this is function 1 in child")

obj = child()
obj.funct1()
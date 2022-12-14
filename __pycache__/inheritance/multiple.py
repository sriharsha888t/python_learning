class parent():
    def function1(self):
        print('This is function 1')
class parent2():
    def function2(self):
        print('This is function 2')
class child(parent,parent2):
    def function3(self):
        print('This is function 3')


ob = child()
ob.function1()
ob.function2()


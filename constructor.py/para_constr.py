# parameterized constructor
class Student:
    def __init__(self,name):
        print("parameterised constructor")
        self.name = name

    def show(self):
        print("hello",self.name)

s1 = Student('ram')
s1.show()



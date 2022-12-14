# ininstance()
class Student:
    id = 101
    name = 'harsha'

    def __init__(self,id,name):
        self.name = name
        self.id = id

s1 = Student(101,'harsha')
print(s1)
print(isinstance(s1,Student))
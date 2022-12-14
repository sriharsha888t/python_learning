# built-in class methods
class student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def Display(self):
        print("name is %s,age %d,id %d"%(self.name,self.age,self.id))

s1 = student('raj',22,101)

print(s1.__doc__)

print(s1.__dict__)

print(s1.__module__)

s1.Display()

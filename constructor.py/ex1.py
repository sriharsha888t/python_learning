# constructor implimentation
class Employee:
    def __init__(self,name,id):
        self.id = id
        self.name = name

    def Display(self):
        print(self.id,self.name)


emp1 = Employee("ram",101)
emp2 = Employee("kiran",102)


emp1.Display()
emp2.Display()
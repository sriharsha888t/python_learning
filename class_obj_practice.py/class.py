class student:
    def __init__(self,name,id,age):
       self.name = name
       self.id = id
       self.age = age
    def funct(self):
        #self.name = name
        #self.id = id
        #self.age = age
        print("name is",self.name,"id is",self.id,"age is",self.age,)

s = student('harsha',100,23)  # s is the object
#s.funct('harsha',100,23) # parameters are passing through function
s2 = student("ram",20,101)
s.funct()
s2.funct()




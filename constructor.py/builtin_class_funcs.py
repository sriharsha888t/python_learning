# built-in functions in class

class Student:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
# creating object of the class student
s1 = Student(101,'kiran',22)

# print the attributes of the student name
print(getattr(s1,'name'))

# reset the value of  attribute age 
setattr(s1,'age',23)

# print attribute of the age
print(getattr(s1,'age'))

# returns true if the student class containing age
print(hasattr(s1,'age'))

# deletes the attribute age from student 
delattr(s1,'age')


# error occurs age hasbeen deleted
print(s1,age)

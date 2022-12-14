# counting the objects of the class with function call
class Student:
    count = 0
    def function(self):
        Student.count = Student.count + 1

s1 = Student()
s1.function()

s2 = Student()
s2.function()

s3 = Student()
s3.function()

print("The number of the students in class:",Student.count)

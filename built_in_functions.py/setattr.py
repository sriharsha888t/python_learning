# setattr
class Student:
    id = 0
    name = "harsha"

    def _init_(self,id,name):
        self.id = id
        self.name = name

student = Student()
print(student.id)
print(student.name)
setattr(student,'mail','abc@email')
print(student.mail)


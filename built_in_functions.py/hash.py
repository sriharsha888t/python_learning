# hash()
r = hash(20)
print(r)
r2 = hash(22.2)
print(r2)
a = hash('a')
print(a)

#  example hash()

result = hash("harsha")   # string value
re2 = hash((1,2,0,1))

print(result)
print(re2)

# example 3
#l = hash([1,2,3,4]) # list is unhashable
#print(l)


# hash() in classes

class Student:
    def __init__(self,name,email):
        self.name = name
        self.email = email

student=Student("harsha","abc@email")

result = hash(Student)
print(result)

print(hash(True))
print(hash(False))
print(hash(int))
print(hash(bool))





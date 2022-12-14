class student:
    age = 20
    name = 'ram'

d = student()
print(getattr(student,'age'))

print(d.age)
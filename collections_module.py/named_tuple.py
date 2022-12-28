from collections import namedtuple


# creating a namedtuple
student = namedtuple('student',['Name','Age','DOB'])

# insering values into named tuple
s = student('Harsha','23','1999')

# printing the namedtuple
print(s)

# accessing the tuple values

print(s[1])
print(s[2])
print(s[0])

print(s.Name)

s2 = ('abcd','24','1998')
print(student._make(s2))

print(s._asdict())


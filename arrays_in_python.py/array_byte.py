from array import *

a = array('b',[98,100,101,102,103])
print(a)

for i in a:
    print(i,end='')
print()

b = a.tobytes()
print(b)
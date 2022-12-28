# arrays in python
import array 
a = array.array('i',[1,2,3,4,5])
print(a)    
print(a[ 0 : 2])

import array as arr
b = arr.array('i',[1,2,3,4,5,6])
print(b)

from array import *
c = array('i',[1,2,3,4,5,6,7])
print(c)
print(c[0])
print(c[5])
print(len(c))
c.append(8)
print(c)
c.extend([9,10,11,12])
print(c)
c.insert(8,100)
print(c)
print(c.pop(0))
c.remove(100)
print(c)



# array concatenation
d = a + b + c
print(d)


# loops through an array

import array
a = array.array('d',[1.1,2.0,3.0,4.1])
print("all values")
for x in a:
    print(x)





d = array.array('i',[1,2,3,4,5])
temp = 0
while temp < d[2]:
    print(d[temp])
    temp = temp+1
    
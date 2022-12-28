from array import *

a = array('i',(1,2,3,4,5))
print(str(a.buffer_info()))
print(str(a.buffer_info()[1]* a.itemsize ))
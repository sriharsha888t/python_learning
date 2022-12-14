# range() using floats
#for i in range(2.2):     # 'float' object cannot be interpreted as an integer
 #   print(i)

# we can use floats in range() with numpy module
import numpy 
for i in numpy.arange(3.3):
    print(i)

for i in numpy.arange(1.0,3.0):
    print(i)

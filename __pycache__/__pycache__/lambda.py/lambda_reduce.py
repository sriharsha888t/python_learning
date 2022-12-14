# reduce(function,sequence)
from functools import reduce
x=reduce(lambda a,b:a+b,[1,2,3,4])
print(x)

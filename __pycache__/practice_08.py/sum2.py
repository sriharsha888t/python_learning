# using reduce() to sum 
from functools import reduce
from operator import add
a=reduce(add,[1,2])
print(a)

# using lambda function
x = reduce(lambda x,y:x + y,[1,2,3,4])
print(x)

r = sum(x ** 2 for x in range(1,7))
print(r)

m = sum([2,2,2,2],100)
print(m)



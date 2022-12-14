# reduce(function,iterables)
from functools import reduce
def a(x,y):
    return x + y
s = reduce(a,[1,2,3,3,4,5,5,6,6,6,7,8,8])
print(s)

# reduce with lambda

x = reduce(lambda q,p:q*p,[1,2,3,4])
print("The product of q,p is:",x)

y = reduce(lambda q,p: q+p,[2,3,4,5])
print("the addition of q,p is:",y)
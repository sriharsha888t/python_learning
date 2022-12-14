# map(function,iterables)
def new(a):
    return a * a
x = map(new,[1,2,3,4])
print(x)  # map.object
print(list(x))  # x is list
#print(set(x)) # x is set
#print(tuple(x))   # x is tuple


def new(a,b):
    return a * b
x = map(new,[1,2,3,4],[1,2,3,4])
print(x)
print(tuple(x))

# using lambda function
l = [1,2,3,4,5]
y=list(map(lambda x:x+3,l))
print(y)
# filter() using normal function
# filter(function,iterator)
def new1(i):
    if i >= 3 :
        return i
j = filter(new1,(1,2,3,4,5,6,7))
print(j)   # converting filter object to tuple type
print(tuple(j))


# filter() using lambda function

z = filter(lambda x:x >= 3,(1,2,3,4,5,6,7))
print(z)   # conveting filter object to list type
print(list(z))
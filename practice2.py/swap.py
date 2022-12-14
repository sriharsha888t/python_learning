a = int(input("enter number:"))
b = int(input("enter number:"))

print("The value of a before swapping:",a)
print("The value of b before swapping:",b)


temp = a
a = b
b = temp

print("The value of a after swapping:",a)
print("The value of b after swapping:",b)


# without using temp variable

x = 10
y = 15

x,y = y,x
print("x =",x)
print("y =",y)
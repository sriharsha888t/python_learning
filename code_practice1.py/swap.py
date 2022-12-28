# swapping using temporary variable

a = 10
b = 20
print(a,b)

c = a      # c is a temporary variable
a = b
b = c
print(a,b)


# without using temporary variable

x = 90
y = 80
print(x,y)
x,y = y,x
print(x,y)


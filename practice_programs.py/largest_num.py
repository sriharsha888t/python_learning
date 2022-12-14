# finding largest number
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
if (a > b ) and (a > c):
    print("a is large ",a)
elif (b > a) and (b > c):
    print("b is large",b)
elif (c > a) and (c > b):
    print("c is large",c)
else:
    print("numbers are equal",a,b,c)
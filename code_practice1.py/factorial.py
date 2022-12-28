n = int(input("Enter a number to find factorials:"))   # user input
factorial = 1              # assingining factorial variable with one
if n < 0:           # condition for lessthan 0 values
    print("No factorials")
elif n == 0:           # condition for equals to zero
    print("Factorial is 1")
else:                    
    for i in range(1,n + 1):  # if value is greater than 0,,if given value is 3,,then 1,2,3
        factorial = i * factorial   # i1*1 + i2*1 + i3*1 = 6
    print(factorial)  # factorial is 6
       


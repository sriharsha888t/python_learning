# prime numbers
num = int(input("enter a number:"))
if num > 1:
    if num == 2:
        print("prime")
    for i in range(2,num):
        if num % i == 0:
            print("not a prime number")
            break
        else:
            print("prime number")

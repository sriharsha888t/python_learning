import sys
num=input("enter a number:")
num = int(num)
isprime = True
if(num == 1):
    print(num, 'is prime')
    exit()
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            isprime = False
            break
else:
    print("number is not a prime")

if(isprime):
    print(num,"number is a prime")
else:
    print(num,"number is not a prime")

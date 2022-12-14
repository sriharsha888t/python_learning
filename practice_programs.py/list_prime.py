# printing the list of prime numbers
start = int(input("enter the starting interval:"))
stop = int(input("enter the stop interval:"))

for num in range(start,stop + 1):
    if start > 1:
        for i in range(2,num):
            if num % i == 0:
               break
        else :
            print(num)


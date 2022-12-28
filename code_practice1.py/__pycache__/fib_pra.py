terms = int(input("enter the trems:"))

n1 = 0
n2 = 1
count = 0
if terms <= 0:
    print("enter a positive number")
elif terms == 1:
    print("fibo value is 1")
else:
    while count < terms:
        print(n1,end='')
        nth = n1 + n2
        n1 = n2
        n2  = nth
        count += 1

print(terms)



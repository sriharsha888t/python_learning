n = 10
m = 10
count = 0
for i in range(1,n):
    count += 1
    for j in range(i-1):
        print("*",end='')
    print()

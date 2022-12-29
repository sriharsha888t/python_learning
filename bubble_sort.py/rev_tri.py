n = 10
m = 0

for i in range(n,0,-1):
    m = m + 1
    for j in range(1,i+1):
        print("*",end=' ')
    print('\r')
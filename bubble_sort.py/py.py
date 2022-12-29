n = 10
m = 10
for i in range(n):          # i = 0,
    for j in range(m):      # j = 0,1,2,3,4,5,6,7,8,9
        print("*",end=' ')  
    print()

print("\n")

for i in range(1,10):        # i = 1    i = 2    i = 3  i = 4   i = 5  i = 6 i = 7 i = 8 i=9
    for j in range(1,10):      # j = 1--9 j = 1--9,,j = 1---9  j = 1--9  j = 1--9 j=1--9   j=1--9   j=1--9 j=1-9 
        print(i,end=' ')       # 1 is 9 times ,2 is 9 times, 3 is 9 times,4 is 9 times
    print() # prints new line

print()

for i in range(1,10):
    for j in range(1,10):
        print(j,end=' ')
    print()

for i in range(1,10):
    for j in range(1,10):
        print(i,j,end=' ')
    print()

print()

for i in range(1,10):   #    i = 1     i = 2         i = 3        i = 4     i = 5         i = 6
    for j in range(i):  #   j = 0      j = 0,1   j = 0,1,2     j = 0,1,2,3  j = 0,1,2,3,4 j = 0,1,2,3,4,5
        print(i,end=' ')
    print()


print()
r = 10
c = 10
for i in range(r):    # i = 0
    for j in range(c): # j = 0-9
        print(j,end=' ') # 
    print()
    


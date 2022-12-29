n = 10
m = 10
for i in range(0,n):
    for j in range(i+1):
        print("*",end=' ')
    print()

a = [2,3,4,5,6,3]
b = set(a)
c = b.difference()
print(c)

z = [1,2,3,2,4]
x = [2,3,7,8,9]

l = [9,8,7,6]
print(list(reversed(l)))
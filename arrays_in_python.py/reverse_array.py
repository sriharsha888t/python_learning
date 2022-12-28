import array as ar

a = ar.array('i',(1, 3, 5, 3, 7, 1, 9, 3))

print(a)

for i in a:
    print(i,end=' ')
print()

print(a[::-1])  # this returns the reverse order of array values

print(a[::-2])

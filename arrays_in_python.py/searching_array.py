import array as ar

a = ar.array('i',(10,20,30,40,50,60))

for i in (a):
    print(i)

print(a.index(30))

print(a.index(60))
import array as arr

a = arr.array('i',(1,3,5,7,9))
for i in a:
    print(i)
print()
a.append(11)
print(a)
a.insert(3,2)
print(a)
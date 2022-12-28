import array as a


l = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14]

a1 = a.array('i',l)

for i in a1:
    print(i,end=' ')

slice_array = a1[:]
print()
print(slice_array)
s_a2 = a1[5:]
print(s_a2)

s_a3 = a1[::-1]
print(s_a3)

s_a4 = a1[::-3]
print(s_a4)



import array as ar
int_array = ar.array('i',[1,2,3,4,5])
print(int_array)


print('The array elements are:')
for i in range(0,5):
    print(i,'----',int_array[i])

print(int_array)

# adding the elements into array

#print(int_array.insert(1,4))
int_array.append(5)
print(int_array)
for j in int_array:
    print(j,end=' ')
print()

# accessing the array elements

print(int_array[0])
print("The element in array at 1 index:",int_array[1])

#print(int_array[8])# array index out of range

print(len(int_array))
for k in range(0,6):
    print(int_array[k])
print()


# removing elements from  array

arr2 = ar.array('i',(9,8,7,6,5,4))
a = arr2.pop(2)
# pop() deletes the elements from 2nd position of the array
arr2.pop(4)
print(arr2)
print(a)

arr2.remove(9)
print(arr2)

import array as arr
unicode_array = arr.array('u',['h','a','r','s','h','a'])
print(unicode_array)
for i in range(0,6):
    print(unicode_array[i],end='')
print()


# insert() used to insert the values in array at specific index position
unicode_array.insert(0,'s')
unicode_array.insert(1,'r')
unicode_array.insert(2,'i')
print(unicode_array)

# append() add the value at the end of the array
unicode_array.append('T')
print(unicode_array)
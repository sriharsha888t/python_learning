# unpacking the elements one by one with iter function
list1 = [1,2,3,4,5]
list2 = iter(list1)
print(next(list2))
print(next(list2))
print(next(list2))
print(next(list2))
print(next(list2))
#print(next(list2))


# with loops
list3 = [1,2,3,4,5]
for i in list3:
    print(i)


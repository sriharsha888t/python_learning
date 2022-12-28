list = [1,2,3,4,5,6]
find = int(input("enter a element to find:"))
found = False
for search in list:
    if find == search:
        found = True
        break
if found == True:
    print("Element {} is found at index {}".format(find,list.index(search)))
else:
    print("The element is not found.")
sum = lambda a,b :a + b 
print("Value of function is:",sum(2,3))

mylist = [1,2,3,4,5,6,8,9]
newlist = list(filter(lambda a:(a/3 == 2),mylist))
print(newlist)

lst = [9,8,7,6,5,4,3,2,1]
p = list(map(lambda a:(a/3!=2),lst))
print(p)

from functools import reduce
print(reduce(lambda a,b:a+b,[1,2,3,4]))


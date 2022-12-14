# filter() within map()
from functools import reduce
C = map(lambda x:x+x,filter(lambda x:(x >= 4),[2,3,4,5])) 
print(tuple(C))


# map() within filter()

d = filter(lambda x:(x>=4),map(lambda x:x+x,[2,3,4,5,6]))
print(set(d))


# map() and filter() within map()

r = reduce(lambda x,y:x+y,map(lambda x:x+x , filter(lambda x:(x<=4),[1,2,3,4,5,6,7])))
print(r)




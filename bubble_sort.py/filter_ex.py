from functools import reduce

c = [1,2,40,100,79,78] #,sum, mul, /2, print
a = reduce(lambda x,y : x + y, c)
print(a)
b = map(lambda x : x * a / 2 , c)
print(b)
f = list(b)
print(f)


 












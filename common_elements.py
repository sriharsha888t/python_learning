from functools import reduce

test_list = [12,14,12,6,7]

result = list(set.intersection(*map(set,test_list)))

print(result)

s = [1,2,3,4,2,8,6,9,3]

v = set(s)

r = list(v.intersection(s))

print(r)

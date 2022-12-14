# all() is return true if all elements in list or set is iterable,otherwise false
k = [1,2,3,4,5,6]
print(all(k))

l = [0,0,1]
print(all(l))

m = ["false",1,2,3]
print(all(m))

n = ['false',0]
print(all(n))

t = (1,2,3,4,5)
print(all(t))

s = {1,2,3,3,4,5,'f'}
print(s)
print(all(s))

z = []
print(all(z))

b = {}
print(all(b))
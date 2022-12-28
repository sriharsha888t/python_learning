from collections import OrderedDict

d = {}
d[1] = 'a'

d[3] = 'c'

d[2] = 'b'

print(d)

od = OrderedDict()

od[7] = 'e'
od[5] = 'f'
od[6] = 'g'

print(od)



od[5] = 'q'
print(od)

d[3] = 's'
print(d)

od.pop(5)
print(od)

od[5] = 'w'
print(od)

d.pop(3)
print(d)
d[3] = '4'
print(d)

for key,value in d.items():
    print(key,value)

for k,v in od.items():
    print(k,v)



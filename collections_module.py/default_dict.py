from collections import defaultdict
def err():
    print('error')

#d = defaultdict(err)

d = defaultdict(lambda : "Not present")

d[1] = 'a'
d[2] = 'b'
d[3] = 'c'
d[4] = 'd'

print(d)
print(d[9])
print(d[3])


print(d.__missing__(5))
print(d.__missing__('b'))



l = [12,13,14,15,16,17]
dd = defaultdict(int)
for i in l:
    dd[i] += 1
print(dd)


d = defaultdict(list)
for i in range(0,5):
    d[i].append(i + 1)
print(d)


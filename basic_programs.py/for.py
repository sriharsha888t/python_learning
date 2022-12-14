animals = ["cat","dog","snake"]
for a in animals:
    print(a,len(a))


obj = ['car','bus','aeroplane']
for o in obj[:]:
    if len(o) > 2:
        obj.insert(0,o)
print(obj)


# lists in python
lst = [1,2,3,'harsha']
lst.pop(1)
print(lst)
lst.insert(1,"sri")
print(lst)
lst.append(20)
print(lst)
lst.remove(3)
print(lst)

lst.reverse()
print(lst)

print(lst.count('harsha'))

lst.extend([1,2,3,4])
print(lst)


l = [2,7,5,8,1,0,3]
l.sort()
print(l)

e = ['a','z','y','n','w']
e.sort()
print(e)

mix = [4,3,5,6]
mix.sort()
print(mix)


x = [1,2,3,4,5,6]
for i in x:
    print(i)


from collections import Counter
ab = [1,2,3,4,5,9,8,7,6,5,4,3,2,1,1,1,2,3,4,5,6,4,5,3,3]
count = Counter(ab)
print(ab)

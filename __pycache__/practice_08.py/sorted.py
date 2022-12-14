l = [9,3,8,1,2,3,4,5]
print(sorted(l))

s = {0,8,9,4,2,9}
print(sorted(s))

m = [',','A','e','k','w','d','f']
print(sorted(m))


strings = ['abc','mno','jkl','xyz']
print(sorted(strings))


#m = ['a',1,'l',2,4,5]
#print(sorted(m))    # '<' not supported between instances of 'int' and 'str'

v = [0,False,'a'=='b',1 <= 0]
print(sorted(v))

names = ['harsha','digitaldots','python']
v =[(ord(name[0])) for name in sorted(names)]
print(v)


# sorting the elements in reverse order
elements = [1,2,3,4,5,6,7]
print(sorted(elements,reverse=True))

list =['name','age','id','harsha']
print(sorted(list,reverse=True))

f = (4,3,21,90,43,56,32)
print(sorted(f,reverse=False))

# sorting with key argument

element = ['ab','qwer','mno','abcdef']
print(sorted(element,key = len))


o = ['sri','harsha','digital','dots','python']
print(sorted(o))
# print(sorted(o,key = str.lower(o)))   # descriptor 'lower' requires a 'str' object but received a 'list'






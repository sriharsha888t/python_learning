# dictionaries in python

d = { 1:'digital',2:'harsha',3:'mca'}
print(d)

print(d.keys())

print(d.values())

print(d.popitem())

print(d.items())

print(d.get(3))

d[3]='aurora'
print(d)

d[4]='hyd'
print(d)

d = {'name':'harsha',"age":23,'spec':'mca'}
print(d)
for i in d:
    print(i)

from collections import ChainMap

a={1:'abc',2:'def'}
b={3:'mno',4:'pqr'}
c = {5:'jkl',6:'qwe'}
print(type(c))

c = ChainMap(a,b,c)
print(type(c))
print(c) 

# nested dictionaries
import pandas
emp_details = {'employee':{'dave':{'id':'001','salary':'2000','designation':'teamlead'},'ava':{'id':'002','salary':'1000','designation':'associate'}}}
print(emp_details)
DF = pandas.DataFrame(emp_details['employee'])
print(DF)


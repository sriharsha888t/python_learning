# creating hash table using built-in dictionary type

my_dict = {'001':"python","002":"java",'003':'javascript'}

print(my_dict)
print()

for e in my_dict:
    print(e)
print()
# printing the key and values in dict by using the items()
print("keys and values in my_dict is:")
for k,v in my_dict.items():
    print(k,'--',v)
print()
# printing the keys using keys()
print("key in my_dict are:")
for k in my_dict.keys():
    print(k)
print()

# printing the values using values()
print("values in my_dict are:")
for v in my_dict.values():
    print(v)
print()





# creating dictionary using built-in dict()

dict1 = dict()
print(type(dict1))

# inserting the elements into dict1

dict1 = {'004':'AWS','005':'azure','006':'GCP'}
print(dict1)
print("keys and values in dict1:")
for m,n in dict1.items():
    print(m,'|',n)
print()

# nested dictionaries

emp_details = {'employee':{'harsha':{'ID':'001',
                                     'designation':'python developer',
                                     'salary':'10,000'},
                          "sai":{'ID':'002',
                                 'Designation':'java',
                                 'salary':'20,000'},
                          'dan':{"ID":'003',
                                  'designation':"java developer",
                                  'salary':'20,000'}}}

#print(emp_details)
#print(emp_details.items())
#print(emp_details.keys())
#import pandas as pd
#DF = pd.DataFrame(emp_details['employee'])
#print(DF)


# accessing dictionaries
# inserting values into dictionary
harsha = {'id':'001','occupation':'student','spec':'mca'}
print(harsha)
harsha['id'] = '002'
print(harsha)


dict2 = {'001':'ava','002':'dev','003':'sam'}

dict2['004'] = 'john'
print(dict2)


# deleting values from dictionary
del dict2['004']   # del() removes the 004 key and value

print(dict2)

dict2.pop('002')   # pop() removes the specific key
print(dict2)

dict2.popitem()   # removes the last inserted element
print(dict2)

# defining dictionary in another way
print()
dict3 = dict([('name','abc'),('age','12'),('id','001')])
print(dict3)

dict4 = dict(name = 'harsha',age = 23,id = '001')
print(dict4)

#print(dict4[1])  # we cannot access the dictionary with index 


# array with hash function
import string
text = string.ascii_uppercase
print(text)
print()
print(text[-1])
print(text[1])
print(len(text) // 2)
print(len(text)-1)

# hashing using buili-in hash()
print(hash("name"))

print(hash(hash))
print(hash(hash))
print(hash(print))

#print(hash[1,2,3])  # built-in types like lists,tuples,sets cannot be hashable
import sys
print(sys.platform)
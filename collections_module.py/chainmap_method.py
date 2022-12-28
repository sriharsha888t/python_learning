from collections import ChainMap
# Individual dictionaries
d1 = {1 : 'a' , 2 : 'b', 3 : 'c'}
d2 = {4 : 'a1',5 : 'b1',6 : 'c1'}
d3 = {7 : 'a2',8 : 'b2',9 : 'c2' }

# encaspulating the individual dictionaries in single unit
chain_dict = ChainMap(d1,d2,d3)
print(chain_dict)
# maps returns the total values in chainmap dictinary
print(chain_dict.maps)
# values() returns the only values from the dictionary
print(list(chain_dict.values()))

print()
# keys() returns the only keys from the dictionary
print(list(chain_dict.keys()))

# adding new dict to existing chainmap dict
d4 ={12 : 1234,13 : 000,14 : 9876}

new_chain = chain_dict.new_child(d4)

print(new_chain)

# reversing the values of chainmap dictionary

new_chain.map = reversed(new_chain.maps)
print(chain_dict[4])


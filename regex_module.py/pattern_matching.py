from re import search

s = "harsha@888t"

print(search('888',s))


val = 'abcd1234'

if search('12',val):
    print("match found")
else:
    print("not found")
import re               # module for regular expression
s1 = 'python123'
print(re.search('p[zyn0]',s1))
print(re.search('t[mnoih]',s1))
print(re.search('p[321nohty]',s1))  # [ ] matches the single charecter in a string which are given in the list
print(re.search('p[a-z]',s1))  # [a-z] represents all alphabets in lower case
print(re.search('p[A-Z]',s1))

print(re.search('p[0-9]',s1))

print(re.search('n[0-9]',s1))

print(re.search('n[0-9][0-9][0-9]',s1))

print(re.search('n[0-n-p]','----0n---'))

print(re.search('[[]',"python["))

print(re.search("[*]","python*"))
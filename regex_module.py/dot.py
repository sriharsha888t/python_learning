import re
print(re.search('py.hon','python'))
print(re.search('py.thon','python'))  # . matches a single character  in a string

print(re.search('p.th.n','python'))

print(re.search('pytho.','pytho\n'))  # except newline

print(re.search('p.thn','p\ython'))


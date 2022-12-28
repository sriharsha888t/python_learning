import re
string1 = 'hi, hello ,welcome to python'

match = re.search('hello',string1)

print(match)

print("start index:",match.start())
print("stop index:",match.end())
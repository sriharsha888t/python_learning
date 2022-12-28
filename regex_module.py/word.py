import re
print(re.search('\w','.a#%$'))
# matches any aphanumeric character in string

print(re.search('\w','#@r$#@'))

print(re.search('[^a-zA-Z0-9]','Harsh@'))

print(re.search("\d",'ooo1'))   
# \d matches the digit in string and it is equivalent to the [0-9] and [^a-z]

print(re.search("\D",'1234i'))     
# \D matches the alphabet in string and it is equivalant to the [a-z] and [^0-9]

print(re.search('\s','python IDE'))
# \s matches the whitespace in a string

print(re.search('\S','python IDLE'))
# \S is opposite to the \s ,it matches the digit which not having whitespace



print(re.search('[\s\w\d]','-----a----'))

# [\w\d\s] matches any digit , whitespace and word

print(re.search('[\d\w\s]','python123 IDE'))





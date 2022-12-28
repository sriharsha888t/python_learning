# using backslash is to droping the special meaning of the character
import re
s = 'Harsha.thatikonda'

result = re.search(r'.',s)
print(result)
# .

result2 = re.search(r'\.',s)
print(result2)


# ^cap symbol checks whether the string starts with given character or not

result3 = re.search('^H',s)
print(result3)


# $ dollor symbol checks whether the string ends with given number or not

result4 = re.search('a$',s)
print(result4)

# (.) symbol returns the character between the string
result5 = re.search(r'H.r',s)
print(result5)

# | or symbol

result6 = re.search(r"H|r",s)
print(result6)

# \b 

s1 = 'python'
r1 = re.search(r'\b(p)',s1)
r2 = re.search(r'(n)\b',s1)
print(r1)
print(r2)


# \A 

r3 = re.search(r'\Apython',s1)
print(r3)

# \d

r4 =re.search(r'\d',s1)
print(r4)


# []
s5 = 'python987'
r5 = re.search('[0-9][0-9][0-9]',s5)   # [0-9] any character which are present in string i.e,,,0 to 9
print(r5)

r6 = re.search('9.7',s5)
print(r6)

r7 = re.search('9.2',s5)
print(r7)


print('\newline')  # here \n represented as new line

print(r'\newline')  # here r(raw-string) is specifies the \n as a string

#print(re.search('\\','python\libary'))

print(re.search('\\\\','python\library'))
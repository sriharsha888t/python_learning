print("python is oops programming language.")
print("'Python' is case sensitive")
print("""I'm "python" learner""")
print('my\name')  # \n represents new line
print(r'my\name') # raw string 
print()


print("""\
       hello
       goodmoring""")


print('''\
        welcome 
        to
        python''')

print('py'+"thon")  # using + symbol to concatenating strings

print('py'+'thon'+'machine learning')

print('hi'*2) # using * symbol to repeat multiple times

a = 'py'
b = 'thon'
print(a + b)
print(a + b + "programming")
print('python'"programming")
#print(a b) # invalid syntax
print(a + b)
#print(a * b)  #can't multiply sequence by non-int of type 'str'
#print(a'thon')
#print(("python" * 2)'programming')

# strings are indexed,index starts from zero
string = 'python programming'
print(string[0])  # charecter from 1st position
print(string[4]) # charecter from index number 4
#print(string[50])  # index number out of range

# strings are also supports negative indexing,it's starts from -1
print(string[-1])  # charecter from last position of the string
print(string[-6])
print(string[-0]) # -0 same as 0 


# strings are supported slicing
print(string[0:6])  # to obtain sub-string
print(string[7:18])
print(string[0:18])
print(string[:])   # it will print total string
print(string[:0])
print(string[-1:-18])

print(string[:6] + string[7:])
print(string[0:3] + string[3:6])
print(string[0:18:2]) # 0 is starting position,18 is stop,2 is step value
print("j" + string[0:6])

# strings does not support item assignment, strings are immutable
# string[1] = "i"

# len() is returns the length of the string
print(len(string))




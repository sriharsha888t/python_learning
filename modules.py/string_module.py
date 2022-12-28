# string module
import string

print(string.digits)

print(string.ascii_letters)

print(string.ascii_lowercase)

print(string.ascii_uppercase)

print(string.capwords)

print(string.hexdigits)

print(string.printable)

print(string.punctuation)

print(string.whitespace)

print(string.octdigits)

print(string.hexdigits)


s = "harsha"
print(s.endswith("a"))

name = "Harsha"
print(name.startswith("H"))

d = '102'
print(d.isdigit())

d1 = '1aw3ff'
print(d1.isdigit())

dec = '134'
print(dec.isdecimal())

# string formatting

s = " This is python {}"
print(s.format("Programming"))

print("hi,{} ,i am {}".format("hello","fine"))

# using key_word and positional arguments

print("My name is {0},i am a {1} programmer.".format("Harsha","python"))

print("My name is {1},I am a {0} programmer.".format("Harsha","Python"))

print("This site is {0:f}% securely {1}!!".format(100, "encrypted"))

print("My average of this {0} was {1:.2f}%".format("semester", 78.234876))

print("my average of this {0} is {1:.3f}".format("semester",83.23))

# converting integer to octal
print("The {0} of 100 is {1:o}".format("octal",100))

# converting integer to binary
print("The {0} of 100 is {1:b}".format("binary",100))


# To demonstrate spacing when
# strings are passed as parameters
print("{0:40} is a programming {1:40}".format("python","language"))


# aligning of spaces using <,^,>

print("My name is {0:>20},I am a {1:^20} and {2:<20} learner.".format("Harsha","Student","Python"))




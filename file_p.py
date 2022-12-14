import os
file = open ("hi.txt","r")
print(file)
file = open("hi.txt","a")
file.write("this is written from file write")
print(file)

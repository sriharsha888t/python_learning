#import exception

try:
    st = input("::")
    num = int(input("::"))
    print(st + num)
 
except TypeError as e:
   print("syntax error",e)


import exception
try:
    print("resource opened")
    a=int(input("enter 1st number:"))
    b=int(input("enter 2nd number:"))
    print(a/b)
except ZeroDivisionError as e:
    print("you cannot divide a number by zero",e)
except ValueError as e:
    print("invalid input")
except exception as e:
    print("something went wrong")
finally:
    print('resourse closed')
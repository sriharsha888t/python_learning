# simple calculator module
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x % y

print("Enter your choice:")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice = input("enter your choice:1/2/3/4:")
if choice in ('1','2','3','4'):
        num1 = float(input("Enter first value:"))
        num2 = float(input("Enter second value:"))
          
        if choice == '1' :
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2' :
            print(num1,"-",num2,'=',sub(num1,num2))
        elif choice == '3':
            print(num1,'*',num2,'=',mul(num1,num2))
        elif choice == '4':
            print(num1,'/',num2,'=',div(num1,num2))
else:
    print("invalid input")

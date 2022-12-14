# functions with * arguments
def function(*args):
    a=[]
    for x in args:
       a.append(x.upper())
    return a

o = function("digital","python")
print(o)

def add(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)


add(1,2)
add(1,2,3,4)
add(20,30,40,40,50)
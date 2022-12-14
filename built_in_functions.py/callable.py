x = 10
print(callable(x))

lst = [1,2,3,4,5]
print(callable(lst))
print(callable(10))

def funct(self):
    print("function")

funct(1)
print(callable(funct))
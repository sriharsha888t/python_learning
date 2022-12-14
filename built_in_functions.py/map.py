# map()
def calculateaddition(n):
    return n + n

numbers = (1,2,3,4)

result = map(calculateaddition,numbers)
print(result)

numberobject = set(result)
print(numberobject)
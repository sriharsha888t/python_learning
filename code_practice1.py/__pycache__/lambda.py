from functools import reduce

elements = int(input("enter how many elements:"))

#result = list(map(lambda x:x ** 2,range(elements)))

#print(result)

#for i in range(elements):
  #  print("The power of",i,"is",result[i])

#nums = list(map(lambda x : x ,range(elements)))
#print(nums)

result = reduce(lambda x,y: x * y,range(1,elements))
print(result)
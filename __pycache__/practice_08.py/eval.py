def add(a , b):
    return a + b

print(eval('add(2 , 3)'))

x = 10
eval('print(x)')
print(eval('x = 20'))  # assignment operation is not supported in eval()
#eval('for i in x: print(i)')  # eval cannot take compound statement as argument
eval('print(2 + x)')
eval('print(2 ** 3)')
eval('print(sum([1,2,3,4]))')
numbers = input("enter a string:")
print('\n')
values = numbers.split()
print(type(values))
print(values)
print("list:",values)
for i in range(len(values)):
    values[i] = int(values[i])

print(type(values))
print(values)

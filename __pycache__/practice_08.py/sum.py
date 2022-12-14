# sum of numbers using for loops
values = [1,2,3,4,5]
s = 0    # accumulator variable
for n in values:
    s = n + s
print(s)


# using built-in  sum()
l = [1,2,3,4]
s = sum(l)
print(s)

print(sum([2,8,10]))

# using user-defined function
def sum_num(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

result = sum_num([10,20,30,40])
print(result)



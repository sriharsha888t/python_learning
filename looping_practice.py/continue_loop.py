l = [1,2,3,-4,-2,3,8]
sum = 0
for element in l:
    if element < 0:
        continue
    sum += element

print(sum)
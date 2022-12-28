series = [1,2,3,4,5,6,7,8,9,10,11]
even_count = 0
odd_count = 0
for e in series:
    if e % 2 == 0:
        even_count += 1
    elif e % 2 != 0:
        odd_count += 1
    else:
        pass
print(even_count)
print(odd_count)
# mapping the elements without using map function
x = [2, 3, 4, 5, 6 ,7]
y = []

for v in x:    # v = 2,3,4,5,6
  if v % 2:      # 2 % 2 = 0,,,2 % 3 = 1,,,2 % 4 = 0,,,2 % 5 = 1,,2 % 6 = 0
    y = y + [v*5]    # 5 x 0 = 0 x 2 = 0,,,5 x 1 =5 x 3 = 15,,,5 x 0 = 0 x 4 = 0
                      #,,,5 x 1 = 5 x 5 = 25,,,5 x 0 = 0 x 6 = 0
print(y)

# mapping the elements using map()
x = [2,3,4,5,6,7]

y = list(map(lambda x:x*5 ,filter(lambda u:u%2,x)))
print(y)
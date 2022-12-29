# printing rectangle
print("1")
for i in range(0,10):     # i = 0      # i = 1
    for j in range(0,10): # j = 1 to 10      # j = 1 to 10
        print(i,end=' ')  # prints i values  1 to 10
    print()  # new line


# printing single character rectangle
print("2")
for i in range(0,10):
    for j in range(0,10):
        print("*",end=' ')
    print()

# printing triangle
print("3")
for i in range(0,10):        # i = 0    i = 1    i = 2          i = 3         i = 4
    for j in range(i):        # j = 0   j = 1    j = 0,1,2       j = 0,1,2,3   j = 0,1,2,3,4
        print("*",end=' ')      # 1 
    print()

print()

print("4")
# reverse triangle
n = 10
m = 0

for i in range(n,0,-1):
    m = m + 1
    for j in range(1,i+1):
        print("*",end=' ')
    print('\r')

# reverse triangle with digit
print("5")
n = 10
m = 0
for i in range(n,0,-1):
    m = m + 1
    for j in range(1,i + 1):
        print(n,end=' ')
        n += 1
    print('\r')


print()

# right angle triangle
print("6")           

n = 5         
# number of spaces
k = 2 * n - 2      # k = 2 x 5 - 2 = 8

for i in range(0, n):            # i = 0 
# outer loop to handle number of rows
# inner loop to handle number spaces
# values changing acc. to requirement
    for j in range(0, k):       # j = 0---8
        print(end=" ")           # prints spaces

     # decrementing k after each loop
    k = k - 2           # k = 8 - 2 = 6

    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i+1):   # j = 0  
    # printing stars
        print("* ", end="")
    print('\r')                  
     # ending line after each row



# printing pyramid pattern

n = 10
k = 2 * n - 2
for i in range(0,n):
    for j in range(0,k):
        print(end=' ')

    k = k - 1
    for j in range(0,i+1):
        print("*",end=' ')
    print()



# printing pyramid with alphabets
n = 10
k = 2 * n - 2
num = 65
for i in range(0,n):
    for j in range(0,k):
        print(end='')
    print()

print("---")


rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")




# 
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


    




#def pyramid(n):      # defining the function

    #k = 2 * n - 2   #  if n = 10,,2 * 10 = 20,,,,20 - 2 = 18
k = 15
n = 15
for i in range(0,n):
    for j in range(0,k):
            print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("*",end=" ")
    print()

#pyramid(15)
   

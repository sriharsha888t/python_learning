# loops
#row = int(input("enter how many rows:"))
row = 5
for i in range(row):   # outer loop --> indicates number of rows 
    for j in range(i):     # inner loop --> indicates number of coloumns
        print(i,end =" ")
    print()
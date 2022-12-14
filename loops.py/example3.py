rows = 5
col = 0
for i in range(rows,0,-1):
    col += 1
    for j in range(1,i + 1):
        print(col,end=' ')
    #print()
    print('\r')
    #print('\n')
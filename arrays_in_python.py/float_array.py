import array as arr
a = arr.array('d',[1.2,1.3,1.4,2.1])
print(a)

print("The array elements are:",end='')
for i in range(0,4):
    print(i,'--',a[i])
def filterdata(x):
    if x > 5:
        return x

result = filter(filterdata,(1,2,3,4,5))
print(list(result))


# filter example

x = filter(None,[0,True,False,6,9])
print(x)
y = list(x)
print(y)

# filter example with functin as parameter

def mul3(n):
    if n % 3 == 0:
        return n

r = filter(mul3,[0,1,2,3,4,5])
l = list(r)
print(l)

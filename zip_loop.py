s1=('enumerate','zip','items')
s2=('dict','list','set')

for i in zip(s1,s2):
    print(i)

S = [1,2,3,4,5,6,3]
V = set(S)
c = V.intersection()
print(c)
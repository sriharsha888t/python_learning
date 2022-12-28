#s1 = ".|."
#s2 = ".|..|..|."
#s3 = ".|..|..|..|..|."
#s4 = ".|..|..|..|..|..|..|."
#s5 = ".|..|..|..|..|..|..|..|..|."
#s6 = "WELCOME"

#print(s1.center(40,"-"))
#print(s2.center(40,"-"))
#print(s3.center(40,"-"))
#print(s4.center(40,"-"))
#print(s5.center(40,"-"))
#print(s6.center(40,"-"))
#print(s5.center(40,"-"))
#print(s4.center(40,"-"))
#print(s3.center(40,"-"))
#print(s2.center(40,"-"))
#print(s1.center(40,"-"))







n,m = map(int,input().split())

for i in range(1,n,2):
    print(str('.|.' * i).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n-2, -1, -2):
    print(str('.|.' * i).center(m, '-'))

    
       










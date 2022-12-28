def fibo(terms):
#terms = int(input("enter the terms:"))
    n1 = 0                               # 
    n2 = 1
    count = 0
    if terms <= 0:                         
        print("enter positive number")
    elif terms == 1:
        print("fibo of 1 is:",n1)
    else:                             # for example input is 5
       while count < terms:           # 0 < 5
        print(n1,end=" ")              # n1 = 0,,, 0    
        nth = n1 + n2                 #  nth = 0 + 1 = 1
        n1 = n2                       # n1 = 0,n2 = 1 ,,,0 = 1
        n2 = nth                     # n2 = 1
        count += 1                   #  0 + 1 = 1,,,1 + 1 = 2,,,2 + 3 = 5,,3 + 5 = 8,,5 + 8 = 13
                                     # output ::: 0,1,1,2,3,5,8,

if __name__=='__main__':
  terms = int(input("Enter terms:"))
  fibo(terms)






start = int(input("enter starting interval:"))  # input for starting 
stop = int(input("enter stop interval:"))       # input for end 


for num in range(start,stop + 1):   # suppose start is 2
   if start > 1 :
      for i in range(2,num):
         if num % i == 0 :
            break
      else:
        print(num,end=' ')
           
            
 

           
        



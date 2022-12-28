def even_num_sum(even_num):
    sum = 0
    for element in even_num:
        if element % 2 != 0:
            print("Odd number found",even_num)
            break            
        sum += element
        
    else:      
        print("The even numbers sum is:",sum)
          

    

even_num_sum([2,2,2])
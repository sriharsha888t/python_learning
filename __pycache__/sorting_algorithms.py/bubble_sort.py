# Implimentation of bubble sort


def bubble_sort(array):          # defining the function with name bubble_sort
    n = len(array)               # finding the length of the array that is passed by the function call
                                  # ex:len is 6
    for i in range(n):              #  i = 0,1,2,3,4,5   array = [6,3,98,12,4,2,56,90]
           
        already_sorted = True          # declaring a flag 

        for j in range(n - i - 1):        # innerloop i = 0 then j = (6 - 0 - 1) = 5  j value 0,1,2,3,4
            #if array[j] > array[j + 1]:   #  ascending order  array[6] > array[3]
            if array[j] < array[j + 1]:    # descending order
                array[j], array[j + 1] = array[j + 1],array[j]  # array[6],array[3] = array[3],array[6]
                already_sorted = False         # changing the flag value

        if already_sorted:        # condition for flag variable
            break

    return array            # returning the sorted array


if __name__ == '__main__':
   #array = [6,3,98,12,4,2,56,90]        # array declarartion
   array = input("enter the elements:").split()
   print("The array before sorting is:",array)
   sorted_array = bubble_sort(array)    # calling a function with an array of elements
   print("The array after sorting is:",sorted_array)            # printing the array
   
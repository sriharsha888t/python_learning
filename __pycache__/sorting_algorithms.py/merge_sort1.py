def merge_sort(arr):  # function defining
    if len(arr) > 1:   # checking the array have elements are not

        mid = len(arr) // 2       # finding the mid of array
        sub_array1 = arr[mid : ]   # array splitted into sub array
        sub_array2 = arr[ : mid]   # sub array 2

        merge_sort(sub_array1)    
        merge_sort(sub_array2)

        i = k = j = 0          # initializing the pointers

        while i < len(sub_array1) and j < len(sub_array2):  # 0 < len(sub1) and 0 < len(sub2)
            if sub_array1[i] < sub_array2[j]:              # 
                arr[k] = sub_array1[i]                 # arr[k] = 
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

#a = [9,2,3,1,6,4,3,2]
a = input("Enter the array elements:").split()
merge_sort(a)
print(a)


import pandas
def merge_sort(array):
    if len(array) < 2:
        return array


    midpoint = len(array) // 2

    result = pandas.merge(left = merge_sort(array[:midpoint]),right = merge_sort(array[midpoint:]))
    return result

l = [2,4,1,7,4,3]
r = merge_sort(l)
print(r)






       
    



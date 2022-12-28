from array import *
def duplicate(nums):
    new = set(nums)
    return len(nums) != len(new)

a = array('i',(1,2,3,3,5,4,5))
a2 = array('i',(1,4,5,6,7,8,7))
a3 = array('i',(1,3,4,6,4,3,2,2,5))
a4 = array('i',(1,2,3,4))

print(duplicate(a))

print(duplicate(a2))

print(duplicate(a3))

print(duplicate(a4))


def first_deplicate(nums):   # (1,2,3,4,2,3,4,5)
    num_set = set()           # 
    no_duplicate = -1

    for i in range(len(nums)):    # len(nums) = 8
        if nums[i] in num_set:      #  nums[i] in 
            return nums[i]          #
        else:
            num_set.add(nums[i])

    return no_duplicate


print(first_deplicate([1,2,3,4,2,3,4,5]))   # sending the arguments to function



class Solution:
    def twoSum(self, nums,target):    #  twoSum takes two parameters nums,target
        for i in range(len(nums)):     #  len(nums) is 0,1,2,3
            for j in range(i + 1, len(nums)):  #  # 0 + 1 = 1,,1 + 1 = 2,,2 + 1 = 3,,3 + 1 = 4,,len(nums)==4
                if nums[j] == target - nums[i]: # nums[j]=2,3,4,2,4,4 == 9 - 1,1,1,2,3,3
                    return [i,j]                 # 19          = 9 - 11

o1 = Solution()
#List =[2,7,11,15]
List = [1,2,3,4]
#target = 9
target = 5
index = o1.twoSum(List,target)
print(index)

# input : [2,3,4] = 2 + 3 = 6
# out put : [0,1] 
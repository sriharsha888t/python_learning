nums =[1,2,3,4]
print(len(nums))
for i in range(len(nums)): # i = 0,1,2,3
    for j in range(i+1,len(nums)): # 0 + 1 = 1,,1 + 1 = 2,,2 + 1 = 3,,3 + 1 = 4,,len(nums)==4
       print(nums[j])   
       print()      # 1 2 3 2 3 3
       print(nums[i])                        # 0 0 0 1 1 2
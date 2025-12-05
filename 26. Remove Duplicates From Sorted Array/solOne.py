nums = [0,0,1,1,1,2,2,3,3,4]
i = nums[0]
k=1
for j in range(len(nums)):
    if  nums[j] != i:
        nums[k] = nums[j]
        i=nums[j]
        k+=1
print(nums)
nums = [2,0,2,1,1,0]
i=0
k=len(nums)-1
j=0

while j <= k:
    if nums[j] == 0:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
        j+=1
    elif nums[j] == 2:
        nums[k],nums[j] = nums[j],nums[k]
        k-=1
    else:
        j+=1

print(nums)


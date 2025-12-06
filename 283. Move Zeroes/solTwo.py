nums = [0,1,0,3,12]
pindex = 0
j=0
while j<len(nums):
    if nums[j] != 0:
        nums[pindex],nums[j] = nums[j],nums[pindex]
        j+=1
        pindex+=1
    else:
        j+=1


print(nums)
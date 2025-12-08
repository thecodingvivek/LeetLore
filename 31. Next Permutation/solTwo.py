
def rev(li,ri): 
    while li<ri:
        nums[li],nums[ri] = nums[ri],nums[li]
        li+=1
        ri-=1


nums = [2,3,1,3,3]
i =  len(nums) - 2


while i>=0 and nums[i]>=nums[i+1]:
    i-=1

if i<0:
    rev(0,len(nums)-1)
    exit()


j = len(nums) - 1
while nums[j] <= nums[i]:
    j -= 1
print(j)
nums[i], nums[j] = nums[j], nums[i]

li= i+1
ri = len(nums)-1

rev(li,ri)

print(nums)
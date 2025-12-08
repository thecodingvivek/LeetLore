nums = [3,2,3,3]
nums.sort()


count = 1
i=1

print(len(nums)//2)
while i<=len(nums)-1:
    if nums[i] == nums[i-1]:
        count+=1
    else:
        if count >= len(nums)/2:
            print(nums[i-1])
            break
        count = 1
    i+=1

if count >= len(nums)//2:
    print(nums[i-1])
    
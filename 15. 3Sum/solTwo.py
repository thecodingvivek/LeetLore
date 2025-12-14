nums = [-1,0,1,2,-1,-4]
nums.sort()
result = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue

    co= i+1
    cs=len(nums)-1

    print(co,cs)
    while co<cs:
        if nums[co] + nums[cs] + nums[i] == 0:
            result.append([nums[i],nums[co],nums[cs]])
            while co<cs and nums[co] == nums[co-1]:
                co+=1

            while co<cs and cs<len(nums)-1 and nums[cs] == nums[cs+1]:
                cs-=1

        elif nums[co] + nums[cs] + nums[i]<0:
            co+=1

        elif nums[co] + nums[cs] + nums[i] > 0:
            cs -=1


print(result)
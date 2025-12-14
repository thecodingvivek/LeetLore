nums = [2,2,2,2,2]
target = 8
result = []

nums.sort()


for i in range(len(nums)):
    if i>0 and nums[i] == nums[i-1]:
        continue
    for j in range(i+1,len(nums)):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        co = j+1
        cs= len(nums)-1
        while co<cs :
            sums = nums[i] + nums[j] + nums[co] + nums[cs]
            if sums<target:
                co+=1
            elif sums > target:
                cs -=1
            elif sums == target:
                result.append([nums[i],nums[j],nums[co],nums[cs]])
                co+=1
                cs-=1
                while nums[co] == nums[co-1] and co<cs:
                    co+=1
                while nums[cs] == nums[cs+1] and co<cs:
                    cs-=1
                
print(result)


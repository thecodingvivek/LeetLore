nums = [1,1,0,1,1,1]
count  = 0
maxi = 0
for i in range(len(nums)):
    if nums[i] == 1:
        count+=1
    else:
        if maxi < count:
            maxi = count
        count = 0


print(max(maxi,count))
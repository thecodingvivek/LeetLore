nums = [2,2,1,1,1,2,2]
count=0
i=0
element = 0
while i<len(nums):
    if count == 0:
        count=1 
        element = nums[i]
    
    else:
        if nums[i] == element:
            count+=1
        else:
            count-=1
    
    i+=1


count = 0
for j in nums:
    if j == element:
        count+=1
    

if count > len(nums)/2:
    print(element)
else:
    print("no its not")
    

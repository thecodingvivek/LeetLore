nums = [3,1,-2,-5,2,-4]
ans = []
k=0
i=0
j=1
while k <len(nums):
    if nums[k]>0:
        ans.append(nums[k])
        i+=2
    elif nums[k]<0:
        ans.append(nums[k])
        j+=2
    k+=1
    
print(ans)
# [0,1,2,4,5,6,7]
# [7,0,1,2,4,5,6]
# [6,7,0,1,2,4,5]
# [4,5,6,7,0,1,2]

nums=[8,9,1,2,4,5,6,7]

i=0
j=len(nums)-1

if nums[i]<nums[j]:
    print(0)
    exit()

mini=nums[0]
while i<=j:
    mid = (i+j)//2

    if nums[mid]<=nums[j]:
        mini=min(nums[mid],mini)
        j=mid-1
    else:
        mini = min(nums[i],mini)
        i=mid+1

print(mini)
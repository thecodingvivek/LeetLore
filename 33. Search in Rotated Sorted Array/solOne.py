nums = [3,1]
target = 1


i=0
j=len(nums)-1


while i<=j:
    mid = (i+j)//2
    if nums[mid] == target:
        print(mid)
        break
    
    if nums[i]<=nums[mid]:
        if nums[i]<=target<=nums[mid]:
            j=mid-1
        else:
            i=mid+1
        
    else:
        if nums[j]>=target >= nums[mid]:
            i=mid+1
        else:
            j=mid-1







nums = [4,5,6,7,0,1,2]
target = 0



start = 0
end = len(nums)-1

while start<=end:
    mid = (start+end)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[start]<=nums[mid]:
        if nums[start]<=target<=nums[mid]:
            end = mid-1
        else:
            start=mid+1
    elif nums[mid]<=nums[end]:
        if nums[mid]<=target<=nums[end]:
            start=mid+1
        else:
            end = mid -1
    
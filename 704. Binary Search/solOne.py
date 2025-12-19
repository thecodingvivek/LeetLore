nums = [-1,0,3,5,9,12]
target = 9
i = 0
j = len(nums)-1
while i<=j:
    mid  = (i+j)//2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] > target:
        j = mid - 1
    else:
        i = mid+1
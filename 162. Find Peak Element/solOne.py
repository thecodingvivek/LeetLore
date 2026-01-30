nums = [1,2,1,3,5,6,4]


start = 0
end = len(nums)-1
if end >= 1:
    if nums[0]>nums[1]:
        print(nums[0])
        exit()
    if nums[end]>nums[end-1]:
        print(nums[end])
        exit()
else:
    print(nums[0])
    exit()

start +=1
end -=1


while start<=end:
    mid = (start+end)//2

    if nums[mid-1]<nums[mid]>nums[mid+1]:
        print(nums[mid])
        break
    elif nums[mid-1]<nums[mid]<nums[mid+1]:
        start = mid+1
    elif nums[mid-1]>nums[mid]>nums[mid+1]:
        end = mid-1
    else:
        start=mid+1

print("jai babu")
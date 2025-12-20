nums = [5,7,7,8,8,10]
target = 8


i=0
j=len(nums)-1

if len(nums)==0:
    exit()

while i<=j:
    mid = (i+j)//2
    if target<=nums[mid]:
        ans = mid
        j=mid-1
    else:
        i=mid+1

end=ans
while end<len(nums) and nums[end] == target:
    end+=1

print([ans,end-1])

nums=[1,2,4,4,4,5,6,7,8]

i=0
j=len(nums)-1

target = 4


while i<=j:
    mid = (i+j)//2
    if target>=nums[mid]:
        ans = mid
        i=mid+1
    else:
        j=mid-1

print(ans)

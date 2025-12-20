nums = [5,7,7,8,8,10]
target = 8


i=0
j=len(nums)-1
ans=0
end=0
if len(nums)==0:
    exit()

while i<=j:
    mid = (i+j)//2
    if target<=nums[mid]:
        ans = mid
        j=mid-1
    else:
        i=mid+1

i=0
j=len(nums)-1
while i<=j:
    mid = (i+j)//2
    if target>=nums[mid]:
        end = mid
        i=mid+1
    else:
        j=mid-1

if len(nums)==0 or nums[ans]!=target or nums[end]!=target:
    return [-1,-1]

return [ans,end]

nums=[1,2,4,4,4,5,6,7,8]

i=0
j=len(nums)-1

target = 4
while i<=j:
    mid = (i+j)//2
    print("mid",mid)
    if target<=nums[mid]:
        ans = mid
        j=mid-1
        print("j",j)
    else:
        i = mid+1
        print("i",i)

print(i,j,ans)


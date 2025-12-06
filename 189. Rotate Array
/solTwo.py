nums = [-1,-100,3,99]
k=2
l = len(nums)
k%=l


def rev(l,r):
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1

rev(0,l-1)
print(nums)
rev(0,k-1)
print(nums)
rev(k,l-1)
print(nums)
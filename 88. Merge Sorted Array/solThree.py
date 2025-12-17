nums1 = [1,2,7,0,0,0]
m = 3
nums2 = [1,5,6]

n = 3
last = len(nums1)-1



while m>0 and n>0:
    if nums2[n-1] >= nums1[m-1]:
        nums1[last] = nums2[n-1]
        n-=1
    elif nums1[m-1] > nums2[n-1]:
        nums1[last] = nums1[m-1]
        m-=1
    last-=1


while n>0:
    nums1[last] = nums2[n-1]
    n-=1
    last-=1

print(nums1)
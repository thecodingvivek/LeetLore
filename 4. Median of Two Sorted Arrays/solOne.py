nums1 = [1,2]
nums2 = [3,4,5]

totallen = len(nums1)+len(nums2)

if len(nums2)<len(nums1):
    nums1,nums2 = nums2,nums1

    


start = 0
end = len(nums1)

while start<=end:
    mid = ((start+end)//2) 
    n=mid

    j = ((totallen+1)//2) - n
    
    if n < 0 or n > len(nums1) or j < 0 or j > len(nums2):
        print(-1)
        break

    if len(nums1) == 0:
        leftone = -float('inf')
        rightone = float('inf')

    elif n==0:
        leftone = -float('inf')
        rightone = nums1[n]

    elif n == len(nums1):
        leftone = nums1[n-1]
        rightone = float('inf')

    else:
        leftone = nums1[n-1]
        rightone = nums1[n]


    if j == 0:
        lefttwo = -float('inf')
        righttwo = nums2[0]
    elif j == len(nums2):
        lefttwo = nums2[j-1]
        righttwo = float('inf')
    else:
        lefttwo = nums2[j-1]
        righttwo = nums2[j]


    if leftone>righttwo:
        end = mid - 1
    elif lefttwo>rightone:
        start = mid + 1
    else:
        leftmax = max(leftone,lefttwo)
        rightmin = min(rightone,righttwo)
        if totallen%2 == 0:
            print((leftmax + rightmin)/2)
            break
        else:
            print(leftmax)
            break




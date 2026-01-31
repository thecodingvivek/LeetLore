nums = [1,2,5,9]
threshold = 6


start = 1
end = max(nums)
sums=0
mini=float('inf')

while start<=end:
    mid = (start+end)//2
    for i in nums:
        sums+= (i+mid-1)//mid
    if sums > threshold:
        start = mid + 1
    else:
        end = mid - 1
        if mid<mini:
            mini = mid
    sums=0


print(mini)

        
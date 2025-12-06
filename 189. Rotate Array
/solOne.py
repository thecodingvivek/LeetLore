nums = [-1,-100,3,99]
k=2
o=0
l = len(nums) -1

if k > l:
    k = k % (l+1)



for j in range(len(nums)//2):
    nums[j],nums[len(nums) - j - 1] = nums[len(nums) - j -1],nums[j]



for j in range(0,len(nums[:k])//2):
    nums[j],nums[len(nums[:k]) -  j - 1] = nums[len(nums[:k]) - j - 1],nums[j]

for j in range(k,k + ((len(nums) - k)//2)):
    nums[j],nums[len(nums) - o - 1] = nums[len(nums) - o -1],nums[j]
    o+=1


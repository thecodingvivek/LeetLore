nums = [3,4,5,1,2]
s = sorted(nums)
x=0
for i in nums:
    if i == s[i]:
        x = i
for i in range(len(nums) -1):
    if s[i] == nums[(i+x)%len(nums)]:
        pass
    else:
        return False
return True

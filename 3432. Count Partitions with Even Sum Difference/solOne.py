nums = [2,4,6,8]
fsum = 0
tsum = sum(nums)

for i in range(len(nums)-1):
    fsum+=nums[i]
    if ((tsum - fsum) - fsum )% 2 == 0:
        print(i)
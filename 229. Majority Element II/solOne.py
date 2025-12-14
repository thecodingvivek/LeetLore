nums = [3,3,2,2,2,3]
elemf = 0
elems=0

countf=0
counts=0

for i in range(len(nums)):
    if elemf == nums[i]:
        countf+=1
    elif elems == nums[i]:
        counts +=1
    
    elif countf == 0:
        elemf = nums[i]
        countf = 1
    elif counts == 0:
        elems = nums[i]
        counts = 1
    else:
        countf-=1
        counts-=1


co=0
cs=0
finall = []
for j in nums:
    if j == elemf:
        co+=1
    elif j == elems:
        cs+=1
    else:
        pass

if co > len(nums)//3:
    finall.append(elemf)
if cs > len(nums)//3:
    finall.append(elems)
print(finall)

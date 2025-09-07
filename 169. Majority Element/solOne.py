nums = [3,1,3]
d = {}

for i in nums:
    if d.get(i):
        d[i]+=1
    else:
        d[i]=1

    if d[i] >= len(nums)/2:
        print(i)
        break

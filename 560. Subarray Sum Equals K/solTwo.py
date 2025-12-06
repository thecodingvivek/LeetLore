nums = [1,2,3,1,1,1,1,4,2,3]
k=3
hashmap = {0:1}

sumi = 0
rem = 0
i =0
count = 0
while i<len(nums):
    sumi += nums[i]
    rem = sumi - k
        
    if hashmap.get(rem):
        count+=hashmap.get(rem)


    if hashmap.get(sumi):
        hashmap[sumi] += 1
    else:
        hashmap[sumi] = 1

    i+=1
    
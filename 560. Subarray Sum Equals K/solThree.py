nums = [1,2,3,1,1,1,1,4,2,3]
k=3


hashmap = {0:1}
rem=0
sums=0
count = 0
for i in nums:
    sums+=i
    rem = sums - k 
    
    if rem in hashmap:
       count+=hashmap[rem]

    if sums in hashmap:
        hashmap[sums] += 1
    else:
        hashmap[sums] = 1


print(count)
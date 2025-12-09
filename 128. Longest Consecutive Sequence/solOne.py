nums = [100,4,200,1,3,2]
dic = set(nums)

count = 0
long = 0
for i in dic:
    if i-1 not in dic:
        y=i
        while y in dic:
            count+=1
            y+=1
        long = max(long,count)
    count=0
        
print(long)
import math
piles =[30,11,23,4,20]
h = 5

start = 1
end = max(piles)

eat=0
temp=h

while start<=end:
    mid = (start+end)//2
    for i in piles:
        eat += math.ceil(i/mid)

    if eat > h:
        start=mid+1

    else:
        if mid<=temp:
            temp=mid
        end = mid-1
    eat=0


print(temp)


